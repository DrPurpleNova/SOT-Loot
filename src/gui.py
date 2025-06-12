from tkinter import Tk, Listbox, StringVar, Entry, Label, Button, OptionMenu, IntVar, messagebox, Frame, Scrollbar, END
from tkinter import ttk
from calc import treasures, emissaries, calculate_loot

from tkinter import Toplevel

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
            # 2 Reaper's Bones Chests: Either Reaper’s Chests or Reaper’s Bounties or one of each
            ("Reaper's Chest", 0, 2),
            ("Reaper's Bounty", 0, 2),
            # 4 random Mermaid Gems
            ("Mermaid Gem", 4, 4),
        ]
    }
}

# Helper to get treasure object by name (handles Mermaid Gems as a group)
def get_treasure_by_name(name):
    if name == "Mermaid Gem":
        # Return all three gem objects
        return [t for t in treasures if "Mermaid Gem" in t.name]
    return [t for t in treasures if t.name == name]

class TreasureCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Treasure Calculator")

        self.selected_treasures = {}
        self.emissary_level = IntVar(value=1)
        self.selected_emissary = StringVar(value=emissaries[0].name)

        # Event multipliers
        self.gold_rush_active = IntVar(value=0)
        self.gold_and_glory_active = IntVar(value=0)

        self.create_widgets()

    def create_widgets(self):
        main_frame = Frame(self.master)
        main_frame.pack(padx=10, pady=10)

        # Preset selection
        preset_frame = Frame(main_frame)
        preset_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        Label(preset_frame, text="Presets:").pack(side="left")
        self.preset_var = StringVar(value="")
        self.preset_menu = OptionMenu(preset_frame, self.preset_var, *PRESETS.keys())
        self.preset_menu.pack(side="left", padx=(5, 0))
        Button(preset_frame, text="Add Preset", command=self.add_preset).pack(side="left", padx=(5, 0))
        Button(preset_frame, text="Add Preset x2", command=lambda: self.add_preset(multiplier=2)).pack(side="left", padx=(5, 0))

        # Left: Search and treasure list
        left_frame = Frame(main_frame)
        left_frame.grid(row=1, column=0, sticky="n")

        Label(left_frame, text="Search Treasures:").pack(anchor="w")

        self.search_var = StringVar()
        self.search_var.trace("w", self.update_treasure_list)
        self.search_entry = Entry(left_frame, textvariable=self.search_var, width=40)
        self.search_entry.pack(anchor="w", pady=(0, 5))

        treasure_list_frame = Frame(left_frame)
        treasure_list_frame.pack()

        self.treasure_listbox = Listbox(treasure_list_frame, selectmode="multiple", width=40, height=20)
        self.treasure_listbox.pack(side="left", fill="y")

        scrollbar = Scrollbar(treasure_list_frame, orient="vertical", command=self.treasure_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.treasure_listbox.config(yscrollcommand=scrollbar.set)

        self.populate_treasure_list()

        add_button = Button(left_frame, text="Add Selected →", command=self.add_selected_treasures)
        add_button.pack(pady=(5, 0))

        # Right: Selected treasures and controls
        right_frame = Frame(main_frame)
        right_frame.grid(row=1, column=1, padx=(20, 0), sticky="n")

        Label(right_frame, text="Selected Treasures:").pack(anchor="w")

        # Pulsante per cancellare tutti i tesori aggiunti
        Button(right_frame, text="Clear All", command=self.clear_selected_treasures, fg="red").pack(anchor="w", pady=(0, 5))

        self.selected_list_frame = Frame(right_frame)
        self.selected_list_frame.pack()

        self.update_selected_treasures_view()

        # Emissary and level
        Label(right_frame, text="Select Emissary:").pack(anchor="w", pady=(10, 0))
        self.emissary_menu = OptionMenu(right_frame, self.selected_emissary, *[e.name for e in emissaries])
        self.emissary_menu.pack(anchor="w")

        Label(right_frame, text="Emissary Level:").pack(anchor="w", pady=(10, 0))
        self.level_spinbox = ttk.Spinbox(right_frame, from_=1, to=5, textvariable=self.emissary_level, width=5)
        self.level_spinbox.pack(anchor="w")

        # Event multipliers (spostati qui sotto Emissary Level)
        Label(right_frame, text="Event Multipliers:").pack(anchor="w", pady=(10, 0))
        self.gold_rush_check = ttk.Checkbutton(right_frame, text="Gold Rush x1.5", variable=self.gold_rush_active)
        self.gold_rush_check.pack(anchor="w")
        self.gold_and_glory_check = ttk.Checkbutton(right_frame, text="Gold & Glory x2", variable=self.gold_and_glory_active)
        self.gold_and_glory_check.pack(anchor="w")

        self.calculate_button = Button(right_frame, text="Calculate Loot", command=self.calculate_loot)
        self.calculate_button.pack(pady=(10, 0), anchor="w")

        self.result_label = Label(right_frame, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(anchor="w", pady=(10, 0))

    def populate_treasure_list(self):
        self.treasure_listbox.delete(0, END)
        for treasure in treasures:
            self.treasure_listbox.insert(END, treasure.name)

    def update_treasure_list(self, *args):
        search_term = self.search_var.get().lower()
        self.treasure_listbox.delete(0, END)
        for treasure in treasures:
            if search_term in treasure.name.lower():
                self.treasure_listbox.insert(END, treasure.name)

    def add_selected_treasures(self):
        selected_indices = self.treasure_listbox.curselection()
        for idx in selected_indices:
            # Find the actual treasure object by name (since list may be filtered)
            name = self.treasure_listbox.get(idx)
            treasure = next((t for t in treasures if t.name == name), None)
            if treasure:
                self.selected_treasures[treasure] = self.selected_treasures.get(treasure, 0) + 1
        self.update_selected_treasures_view()

    def update_selected_treasures_view(self):
        # Clear previous widgets
        for widget in self.selected_list_frame.winfo_children():
            widget.destroy()
        if not self.selected_treasures:
            Label(self.selected_list_frame, text="No treasures selected.").pack()
            return
        for treasure, count in self.selected_treasures.items():
            row = Frame(self.selected_list_frame)
            row.pack(fill="x", pady=2)
            Label(row, text=treasure.name, width=30, anchor="w").pack(side="left")
            Button(row, text="-", width=2, command=lambda t=treasure: self.change_treasure_count(t, -1)).pack(side="left")
            Label(row, text=f"x{count}", width=4).pack(side="left")
            Button(row, text="+", width=2, command=lambda t=treasure: self.change_treasure_count(t, 1)).pack(side="left")

    def change_treasure_count(self, treasure, delta):
        if treasure in self.selected_treasures:
            self.selected_treasures[treasure] += delta
            if self.selected_treasures[treasure] <= 0:
                del self.selected_treasures[treasure]
        self.update_selected_treasures_view()

    def add_preset(self, multiplier=1):
        preset_name = self.preset_var.get()
        if not preset_name or preset_name not in PRESETS:
            messagebox.showwarning("Preset", "Please select a preset.")
            return
        preset = PRESETS[preset_name]
        # Add fixed treasures
        for name, qty in preset.get("fixed", []):
            treasures_found = get_treasure_by_name(name)
            for t in treasures_found:
                self.selected_treasures[t] = self.selected_treasures.get(t, 0) + qty * multiplier
        # Add ranged treasures (min/max logic)
        for name, min_qty, max_qty in preset.get("range", []):
            treasures_found = get_treasure_by_name(name)
            # For Mermaid Gems, distribute for min/max calculation
            if name == "Mermaid Gem":
                # For min: add 1 (or 4) Sapphire (all same value), for max: add 5 Ruby (all same value)
                # Here, add the minimum number of the lowest value gem, and the maximum number of the highest value gem
                # For selection, add the average (rounded down) of the range as Sapphire
                for t in treasures_found:
                    if t.name == "Sapphire Mermaid Gem":
                        self.selected_treasures[t] = self.selected_treasures.get(t, 0) + min_qty * multiplier
            else:
                # For selection, add the minimum quantity (user can adjust after)
                for t in treasures_found:
                    self.selected_treasures[t] = self.selected_treasures.get(t, 0) + min_qty * multiplier
        self.update_selected_treasures_view()

    def calculate_loot(self):
        if not self.selected_treasures:
            messagebox.showwarning("Selection Error", "Please select at least one treasure.")
            return

        # --- Custom min/max logic for presets with randoms ---
        treasure_counts_min = self.selected_treasures.copy()
        treasure_counts_max = self.selected_treasures.copy()

        # Fort of Fortune's Vault: Mermaid Gems 1-5, use Sapphire for min, Ruby for max
        if self.preset_var.get() == "Fort of Fortune's Vault":
            for t in treasures:
                if t.name == "Sapphire Mermaid Gem":
                    treasure_counts_min[t] = treasure_counts_min.get(t, 0) + 1
                if t.name == "Ruby Mermaid Gem":
                    treasure_counts_max[t] = treasure_counts_max.get(t, 0) + 5

        # Fort of the Damned's Vault: 4 random gems, use Sapphire for min, Ruby for max
        if self.preset_var.get() == "Fort of the Damned's Vault":
            for t in treasures:
                if t.name == "Sapphire Mermaid Gem":
                    treasure_counts_min[t] = treasure_counts_min.get(t, 0) + 4
                if t.name == "Ruby Mermaid Gem":
                    treasure_counts_max[t] = treasure_counts_max.get(t, 0) + 4

        min_gain, _ = calculate_loot(
            treasure_counts_min, self.selected_emissary.get(), self.emissary_level.get()
        )
        _, max_gain = calculate_loot(
            treasure_counts_max, self.selected_emissary.get(), self.emissary_level.get()
        )

        # Event multipliers
        multiplier = 1.0
        if self.gold_rush_active.get():
            multiplier += 0.5
        if self.gold_and_glory_active.get():
            multiplier += 1.0

        min_gain *= multiplier
        max_gain *= multiplier

        self.result_label.config(
            text=f"Min Gain: {int(min_gain)} gold, Max Gain: {int(max_gain)} gold"
        )

    def clear_selected_treasures(self):
        self.selected_treasures.clear()
        self.update_selected_treasures_view()
        self.result_label.config(text="")

if __name__ == "__main__":
    root = Tk()
    app = TreasureCalculatorApp(root)
    root.mainloop()