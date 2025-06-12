class Treasure:
    def __init__(self, id, name, min_value, max_value, emissaries):
        self.id = id
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.emissaries = emissaries

class Emissary:
    def __init__(self, name, bonus_per_level):
        self.name = name
        self.bonus_per_level = bonus_per_level

emissaries = [
    Emissary("Gold Hoarders", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
    Emissary("Order of Souls", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
    Emissary("Merchant Alliance", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
    Emissary("Reaper's Bones", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
    Emissary("Athena's Fortune", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
    Emissary("Hunter's Call", {1: 0, 2: 0.33, 3: 0.67, 4: 1.0, 5: 1.5}),
]

treasures = [
    # GOLD HOARDERS - BIG

    # NORMAL
    Treasure(0, "Castaway's Chest", 60, 130, ["Gold Hoarders"]),
    Treasure(1, "Seafarer's Chest", 140, 260, ["Gold Hoarders"]),
    Treasure(2, "Marauder's Chest", 280, 520, ["Gold Hoarders"]),
    Treasure(3, "Captain's Chest", 560, 1100, ["Gold Hoarders"]),

    # CORAL
    Treasure(4, "Castaway's Chest", 105, 228, ["Gold Hoarders"]),
    Treasure(5, "Seafarer's Chest", 245, 455, ["Gold Hoarders"]),
    Treasure(6, "Marauder's Chest", 490, 910, ["Gold Hoarders"]),
    Treasure(7, "Captain's Chest", 980, 1925, ["Gold Hoarders"]),

    # ASHEN
    Treasure(8, "Castaway's Chest", 140, 260, ["Gold Hoarders"]),
    Treasure(9, "Seafarer's Chest", 280, 520, ["Gold Hoarders"]),
    Treasure(10, "Marauder's Chest", 560, 1100, ["Gold Hoarders"]),
    Treasure(11, "Captain's Chest", 1100, 2100, ["Gold Hoarders"]),

    # SPECIAL
    Treasure(12, "Chest of Ancient Tributes", 3400, 3900, ["Gold Hoarders"]),
    Treasure(13, "Chest of the Damned", 1000, 1160, ["Gold Hoarders"]),
    Treasure(14, "Skeleton Captain's Chest", 1150, 1550, ["Gold Hoarders"]),
    Treasure(15, "Stronghold Chest", 1500, 3000, ["Gold Hoarders"]),

    # CURSED
    Treasure(16, "Chest of a Thousand Grogs", 2200, 2600, ["Gold Hoarders"]),
    Treasure(17, "Chest of Sorrow", 3000, 3500, ["Gold Hoarders"]),
    Treasure(18, "Chest of Rage", 3000, 3500, ["Gold Hoarders"]),

    # GOLD HOARDERS - SMALL

    # NORMAL
    Treasure(19, "Ancient Goblet", 60, 130, ["Gold Hoarders"]),
    Treasure(20, "Bronze Secret Keeper", 60, 130, ["Gold Hoarders"]),
    Treasure(21, "Mysterious Vessel", 60, 130, ["Gold Hoarders"]),
    Treasure(22, "Silvered Cup", 140, 260, ["Gold Hoarders"]),
    Treasure(23, "Elaborate Flagon", 140, 260, ["Gold Hoarders"]),
    Treasure(24, "Decorative Coffer", 140, 260, ["Gold Hoarders"]),
    Treasure(25, "Gilded Chalice", 280, 520, ["Gold Hoarders"]),
    Treasure(26, "Ornate Carafe", 280, 520, ["Gold Hoarders"]),
    Treasure(27, "Golden Reliquary", 280, 520, ["Gold Hoarders"]),
    Treasure(28, "Adorned Receptacle", 560, 1100, ["Gold Hoarders"]),
    Treasure(29, "Opulent Curio", 560, 1100, ["Gold Hoarders"]),
    Treasure(30, "Peculiar Relic", 560, 1100, ["Gold Hoarders"]),

    # CORAL
    Treasure(31, "Coral Mysterious Vessel", 105, 228, ["Gold Hoarders"]),
    Treasure(32, "Coral Silvered Cup", 245, 455, ["Gold Hoarders"]),
    Treasure(33, "Coral Golden Reliquary", 490, 910, ["Gold Hoarders"]),
    Treasure(34, "Coral Peculiar Relic", 980, 1925, ["Gold Hoarders"]),

    # ASHEN
    Treasure(35, "Roaring Goblet", 140, 260, ["Gold Hoarders"]),
    Treasure(36, "Brimstone Casket", 280, 520, ["Gold Hoarders"]),
    Treasure(37, "Devil's Remnant", 560, 1100, ["Gold Hoarders"]),
    Treasure(38, "Magma's Grail", 1100, 2100, ["Gold Hoarders"]),

    # ORDER OF SOULS - SKULLS

    # NORMAL
    Treasure(39, "Foul Bounty Skull", 90, 180, ["Order of Souls"]),
    Treasure(40, "Disgraced Bounty Skull", 180, 350, ["Order of Souls"]),
    Treasure(41, "Hateful Bounty Skull", 350, 750, ["Order of Souls"]),
    Treasure(42, "Villainous Bounty Skull", 750, 1450, ["Order of Souls"]),

    # CORAL
    Treasure(43, "Coral Foul Bounty Skull", 158, 315, ["Order of Souls"]),
    Treasure(44, "Coral Disgraced Bounty Skull", 315, 613, ["Order of Souls"]),
    Treasure(45, "Coral Hateful Bounty Skull", 613, 1313, ["Order of Souls"]),
    Treasure(46, "Coral Villainous Bounty Skull", 1313, 2538, ["Order of Souls"]),

    # ASHEN
    Treasure(47, "Ashen Foul Bounty Skull", 180, 350, ["Order of Souls"]),
    Treasure(48, "Ashen Disgraced Bounty Skull", 350, 750, ["Order of Souls"]),
    Treasure(49, "Ashen Hateful Bounty Skull", 750, 1450, ["Order of Souls"]),
    Treasure(50, "Ashen Villainous Bounty Skull", 1450, 2800, ["Order of Souls"]),

    # SPECIAL
    Treasure(51, "Skeleton Captain's Skull", 850, 2200, ["Order of Souls"]),
    Treasure(52, "Stronghold Skull", 1800, 2400, ["Order of Souls"]),
    Treasure(53, "Gold Hoarder's Skull", 10000, 10000, ["Order of Souls"]),
    Treasure(54, "Ashen Winds Skull", 4000, 10000, ["Order of Souls"]),

    # CURSED
    Treasure(55, "Skull of the Damned", 1050, 1250, ["Order of Souls"]),
    Treasure(56, "Captain Skull of the Damned", 1700, 2950, ["Order of Souls"]),

    # MERCHANT ALLIANCE

    # NORMAL
    Treasure(57, "Fruit Crate", 600, 1100, ["Merchant Alliance"]),
    Treasure(58, "Cannonball Crate", 600, 1100, ["Merchant Alliance"]),
    Treasure(59, "Wood Crate", 600, 1100, ["Merchant Alliance"]),
    Treasure(60, "Firebomb Crate", 1100, 2000, ["Merchant Alliance"]),
    Treasure(61, "Ammo Crate", 280, 580, ["Merchant Alliance"]),
    Treasure(62, "Crate of Plants", 700, 700, ["Merchant Alliance"]),
    Treasure(63, "Crate of Luxurious Cloth", 700, 700, ["Merchant Alliance"]),
    Treasure(64, "Crate of Rum Bottles", 700, 700, ["Merchant Alliance"]),

    # CURSED
    Treasure(65, "Storage Crate of the Damned", 900, 1100, ["Merchant Alliance"]),
    Treasure(66, "Cannonball Crate of the Damned", 900, 1100, ["Merchant Alliance"]),

    # CORAL
    Treasure(67, "Coffer of Ancient Grog", 100, 200, ["Merchant Alliance"]),
    Treasure(68, "Coffer of Antiquated Coffee", 260, 470, ["Merchant Alliance"]),
    Treasure(69, "Coffer of Timeworm Metals", 500, 1000, ["Merchant Alliance"]),
    Treasure(70, "Coffer of Forgotten Jewels", 1100, 1900, ["Merchant Alliance"]),

    # ASHEN
    Treasure(71, "Crate of Devil's Plants", 1400, 1400, ["Merchant Alliance"]),
    Treasure(72, "Crate of Devil's Cloths", 1400, 1400, ["Merchant Alliance"]),
    Treasure(73, "Crate of Devil's Rum Bottles", 1400, 1400, ["Merchant Alliance"]),

    # SPECIAL
    Treasure(74, "Prosperous Merchant Mannifesto", 2000, 2000, ["Merchant Alliance"]),
    Treasure(75, "Esteemed Merchant Mannifesto", 2500, 2500, ["Merchant Alliance"]),
    Treasure(76, "Emminent Merchant Mannifesto", 3000, 3000, ["Merchant Alliance"]),
    Treasure(77, "Revered Merchant Mannifesto", 3500, 3500, ["Merchant Alliance"]),

    # GUNPOWDER BARRELS (SOLO MERCHANT ALLIANCE)
    Treasure(78, "Gunpowder Barrel", 150, 350, ["Merchant Alliance"]),
    Treasure(79, "Stronghold Gunpowder Barrel", 3000, 3500, ["Merchant Alliance"]),
    Treasure(80, "Keg of Ancient Black Powder", 5000, 10000, ["Merchant Alliance"]),

    # ATHENA'S FORTUNE

    # CHESTS
    Treasure(81, "Chest of Legends", 10000, 11000, ["Athena's Fortune"]),
    Treasure(82, "Ashen Chest of Legends", 13000, 15000, ["Athena's Fortune"]),
    Treasure(83, "Chest of Boundless Sorrow", 15000, 17000, ["Athena's Fortune"]),
    Treasure(84, "Chest of Fortune", 20000, 25000, ["Athena's Fortune"]),

    # GUNPOWDER BARRELS
    Treasure(85, "Athena's Keg of Ancient Black Powder", 5000, 10000, ["Athena's Fortune"]),

    # SMALLS
    Treasure(86, "Villainous Skull of Ancient Fortune", 4000, 5000, ["Athena's Fortune"]),
    Treasure(87, "Crate of Legendary Voyages", 4000, 5000, ["Athena's Fortune"]),

    # REAPER'S BONES

    # SPECIAL
    Treasure(88, "Reaper's Chest", 10000, 25000, ["Reaper's Bones"]),
    Treasure(89, "Reaper's Bounty", 25000, 25000, ["Reaper's Bones"]),
    Treasure(90, "Cannon of Rage", 250, 250, ["Reaper's Bones"]),

    # MERMAID GEMS (VALGONO PER TUTTE LE FAZIONI PRINCIPALI)
    Treasure(91, "Sapphire Mermaid Gem", 1000, 1000, ["Gold Hoarders", "Merchant Alliance", "Order of Souls", "Hunter's Call"]),
    Treasure(92, "Emerald Mermaid Gem", 1000, 1000, ["Gold Hoarders", "Merchant Alliance", "Order of Souls", "Hunter's Call"]),
    Treasure(93, "Ruby Mermaid Gem", 1000, 1000, ["Gold Hoarders", "Merchant Alliance", "Order of Souls", "Hunter's Call"]),

    # REAPER'S BONES - FLAGS (valore base, emissary value ignorato)
    Treasure(94, "Broken Emissary Flag Grade X (Yours)", 1, 1, ["Reaper's Bones"]),
    Treasure(95, "Broken Emissary Flag (Grade I)", 1600, 2300, ["Reaper's Bones"]),
    Treasure(96, "Broken Emissary Flag (Grade II)", 3500, 4900, ["Reaper's Bones"]),
    Treasure(97, "Broken Emissary Flag (Grade III)", 5500, 6500, ["Reaper's Bones"]),
    Treasure(98, "Broken Emissary Flag (Grade IV)", 7600, 8500, ["Reaper's Bones"]),
    Treasure(99, "Broken Emissary Flag (Grade V)", 9500, 10500, ["Reaper's Bones"]),

    # REAPER'S BONES - NUOVE CASSE E OGGETTI MISSIONE
    Treasure(100, "Casket of Gilded Bones", 5500, 6000, ["Reaper's Bones"]),
    Treasure(101, "Casket of Shadowed Bones", 5000, 5500, ["Reaper's Bones"]),
    Treasure(102, "Casket of Verdant Bones", 4500, 5000, ["Reaper's Bones"]),
    Treasure(103, "Casket of Mottled Bones", 4000, 4500, ["Reaper's Bones"]),
    Treasure(104, "Reaper Master's Urn", 5500, 6000, ["Reaper's Bones"]),
    Treasure(105, "Skull of the Banished", 12500, 12500, ["Reaper's Bones"]),
]

def calculate_loot(treasure_counts, selected_emissary, emissary_level):
    total_min = 0
    total_max = 0
    for treasure, count in treasure_counts.items():
        if selected_emissary == "Reaper's Bones" or selected_emissary in treasure.emissaries:
            bonus = next(e for e in emissaries if e.name == selected_emissary).bonus_per_level.get(emissary_level, 0)
        else:
            bonus = 0
        min_with_bonus = treasure.min_value * (1 + bonus)
        max_with_bonus = treasure.max_value * (1 + bonus)
        total_min += min_with_bonus * count
        total_max += max_with_bonus * count
    return total_min, total_max