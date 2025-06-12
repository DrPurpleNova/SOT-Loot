import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Dropdown, dropdown, Slider
from calc import treasures, emissaries, calculate_loot

# --- Preset definitions ---
PRESETS = {
    "Fort of Fortune's Vault": {
        "fixed": [
            ("Chest of Fortune", 1),
            ("Chest of Legends", 1),
            ("Keg of Ancient Black Powder", 2),
            ("Crate of Legendary Voyages", 4),
            ("Stronghold Chest", 3),
            ("Crate of Ancient Bone Dust", 2),
            ("Stronghold Gunpowder Barrel", 2),
            ("Stronghold Skull", 1),
            ("Captain's Chest", 3),
            ("Trade Good Crate", 3),
        ],
        "range": [
            ("Gilded Chalice of Ancient Fortune", 4, 7),
            ("Chalice of Ancient Fortune", 0, 3),
            ("Villainous Skull of Ancient Fortune", 1, 2),
            ("Skull of Ancient Fortune", 0, 1),
            ("Mermaid Gem", 1, 5),
        ]
    },
    "Fort of the Damned's Vault": {
        "fixed": [
            ("Chest of Legends", 1),
            ("Stronghold Chest", 2),
            ("Crate of Ancient Bone Dust", 2),
            ("Stronghold Skull", 4),
            ("Stronghold Gunpowder Barrel", 4),
            ("Gunpowder Barrel", 4),
        ],
        "range": [
            ("Reaper's Chest", 0, 2),
            ("Reaper's Bounty", 0, 2),
            ("Mermaid Gem", 4, 4),
        ]
    }
}

def get_treasure_by_name(name):
    if name == "Mermaid Gem":
        return [t for t in treasures if "Mermaid Gem" in t.name]
    return [t for t in treasures if t.name == name]

def main(page: ft.Page):
    page.title = "Sea of Thieves Loot Calculator"
    page.window_width = 700
    page.window_height = 500
    page.window_resizable = False
    page.window_max_width = 700
    page.window_max_height = 500
    page.window_min_width = 700
    page.window_min_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # Stato
    onboard_counts = {}
    filtered_treasures = treasures.copy()
    selected_emissary = ft.Ref[ft.Dropdown]()
    selected_level = ft.Ref[ft.Slider]()
    gold_rush = ft.Ref[ft.Checkbox]()
    gold_and_glory = ft.Ref[ft.Checkbox]()
    result_text = ft.Ref[ft.Text]()
    preset_dropdown = ft.Ref[ft.Dropdown]()

    # Funzione per aggiornare la colonna onboard
    def update_onboard():
        onboard.controls.clear()
        for name, qty in onboard_counts.items():
            onboard.controls.append(
                Row([
                    Text(f"{name} x{qty}", width=180),
                    ElevatedButton("-", width=24, height=24, on_click=lambda e, n=name: change_qty(n, -1)),
                    ElevatedButton("+", width=24, height=24, on_click=lambda e, n=name: change_qty(n, 1)),
                ])
            )
        validate()
        page.update()

    # Funzione per cambiare la quantità
    def change_qty(name, delta):
        if name in onboard_counts:
            onboard_counts[name] += delta
            if onboard_counts[name] <= 0:
                del onboard_counts[name]
        update_onboard()

    # Funzione per aggiungere un oggetto
    def add_to_onboard(name):
        if name in onboard_counts:
            onboard_counts[name] += 1
        else:
            onboard_counts[name] = 1
        update_onboard()

    # Funzione per filtrare la lista tesori
    def update_treasure_list(e=None):
        search = text_search.value.lower()
        treasures_col.controls.clear()
        for t in treasures:
            if search in t.name.lower():
                treasures_col.controls.append(
                    ElevatedButton(
                        t.name,
                        on_click=lambda e, n=t.name: add_to_onboard(n),
                        width=250,
                        height=32
                    )
                )
        page.update()

    # Funzione per validare il bottone Calculate
    def validate(e=None):
        button_submit.disabled = len(onboard_counts) == 0
        page.update()

    # Funzione per calcolare il loot
    def submit(e=None):
        treasure_dict = {t.name: t for t in treasures}
        treasure_counts = {}
        for name, qty in onboard_counts.items():
            if name in treasure_dict:
                treasure_counts[treasure_dict[name]] = qty
        em = selected_emissary.current.value
        lvl = int(selected_level.current.value)
        min_gain, max_gain = calculate_loot(treasure_counts, em, lvl)
        multiplier = 1.0
        if gold_rush.current.value:
            multiplier += 0.5
        if gold_and_glory.current.value:
            multiplier += 1.0
        min_gain *= multiplier
        max_gain *= multiplier
        result_text.current.value = f"Min Gain: {int(min_gain)} gold, Max Gain: {int(max_gain)} gold"
        page.update()

    # Funzione per aggiungere preset
    def add_preset(e=None, multiplier=1):
        preset_name = preset_dropdown.current.value
        if not preset_name or preset_name not in PRESETS:
            return
        preset = PRESETS[preset_name]
        # Add fixed treasures
        for name, qty in preset.get("fixed", []):
            treasures_found = get_treasure_by_name(name)
            for t in treasures_found:
                if t.name in onboard_counts:
                    onboard_counts[t.name] += qty * multiplier
                else:
                    onboard_counts[t.name] = qty * multiplier
        # Add ranged treasures (min logic)
        for name, min_qty, max_qty in preset.get("range", []):
            treasures_found = get_treasure_by_name(name)
            if name == "Mermaid Gem":
                for t in treasures_found:
                    if t.name == "Sapphire Mermaid Gem":
                        if t.name in onboard_counts:
                            onboard_counts[t.name] += min_qty * multiplier
                        else:
                            onboard_counts[t.name] = min_qty * multiplier
            else:
                for t in treasures_found:
                    if t.name in onboard_counts:
                        onboard_counts[t.name] += min_qty * multiplier
                    else:
                        onboard_counts[t.name] = min_qty * multiplier
        update_onboard()

    # Funzione per resettare gli onboard treasures
    def clear_onboard(e=None):
        onboard_counts.clear()
        update_onboard()

    # --- UI ELEMENTS ---
    text_search = TextField(label='Search', text_align=ft.TextAlign.LEFT, width=250, on_change=update_treasure_list)
    button_submit = ElevatedButton(
        text='Calculate', width=120, disabled=True, on_click=submit, expand=True
    )

    # Preset dropdown
    preset_dropdown_ctrl = Dropdown(
        ref=preset_dropdown,
        label="Presets",
        width=250,
        value=None,
        options=[dropdown.Option(k) for k in PRESETS.keys()],
    )
    button_add_preset = ElevatedButton(text="Add Preset", width=120, on_click=add_preset)
    button_add_preset2 = ElevatedButton(text="Add Preset x2", width=120, on_click=lambda e: add_preset(e, multiplier=2))

    button_clear_onboard = ElevatedButton(
        text="Clear Onboard", width=120, on_click=clear_onboard, bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE, expand=True
    )

    # Emissary dropdown
    emissary_dropdown = Dropdown(
        ref=selected_emissary,
        label="Emissary",
        width=250,
        value=emissaries[0].name,
        options=[dropdown.Option(e.name) for e in emissaries],
        on_change=validate
    )

    # Emissary level slider
    level_slider = Slider(
        ref=selected_level,
        min=1,
        max=5,
        divisions=4,
        value=1,
        label="{value}",
        width=250,
        on_change=validate
    )

    # Event checkboxes
    gold_rush_checkbox = Checkbox(ref=gold_rush, label="Gold Rush x1.5", value=False, on_change=submit)
    gold_and_glory_checkbox = Checkbox(ref=gold_and_glory, label="Gold & Glory x2", value=False, on_change=submit)

    # Colonna tesori filtrabili
    treasures_col = Column(
        [],
        width=270,
        height=200,
        scroll="auto"
    )

    # Colonna tesori aggiunti
    onboard = Column(
        [],
        width=270,
        height=200,
        scroll="auto"
    )

    # Risultato
    result = Text(ref=result_text, value="", size=16, weight="bold")

    # Inizializza lista tesori
    update_treasure_list()

    # Layout
    page.add(
        Row(
            controls=[
                Column(
                    [
                        text_search,
                        Text("All Treasures:"),
                        treasures_col,
                        emissary_dropdown,
                        level_slider,
                        gold_rush_checkbox,
                        gold_and_glory_checkbox
                    ],
                    width=300
                ),
                Column(
                    [
                        preset_dropdown_ctrl,
                        Row([button_add_preset, button_add_preset2]),
                        Text("Onboard Treasures:"),
                        onboard,
                        Row([
                            button_submit,
                            button_clear_onboard
                        ], expand=True),
                        result
                    ],
                    width=280
                ),
            ],
            alignment=ft.MainAxisAlignment.START
        )
    )

if __name__ == '__main__':
    ft.app(target=main)