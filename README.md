# Sea of Thieves Treasure Calculator GUI

This project is a GUI application for calculating treasure gains in *Sea of Thieves*. It allows players to interactively select emissaries, set levels, choose treasures, and view estimated gold gains using official multipliers.

---

## 🧭 Project Structure

```
sotcalc-gui
├── src
│   ├── calc.py        # Contains the treasure calculation logic
│   ├── gui.py         # Implements the GUI for user interaction
│   └── __init__.py    # Marks the directory as a Python package
├── requirements.txt    # Lists the dependencies required for the project
└── README.md           # Documentation for the project
```

## ✨ Features

- **Searchable Treasure List**: Search dynamically as you type.
- **Emissary Selection**: Choose from available emissaries.
- **Level Selector**: Set your emissary level (1 to 5).
- **Gold Multipliers**: Supports Gold Rush and Gold & Glory bonuses.
- **Preset Support**: Load predefined loot from Fort of the Damned or Fort of Fortune.
- **Real-Time Calculations**: Get instant gold gain estimates (min and max values).

---

## ⚙️ How to Run

### 🔸 Option 1: Download the pre-built `.exe` (recommended for Windows users)

You can download a ready-to-use `.exe` file from the [Releases](https://github.com/DrPurpleNova/SOT-Loot/releases) page.

**Steps:**
1. Go to the [Releases](https://github.com/DrPurpleNova/SOT-Loot/releases).
2. Download the latest `.zip` or `.exe` file (e.g., `SOTCalc.exe`).
3. Extract it (if zipped).
4. Double-click on the `.exe` file to launch the app — **no Python installation needed**.

> ⚠️ Some browsers or Windows SmartScreen may warn you about unknown executables. You can usually click **"More info" → "Run anyway"** if you trust the source.

---

### 🔸 Option 2: Run from source (requires Python)

Make sure you have Python 3.8 or newer installed. Then install dependencies and run the app:

```bash
pip install -r requirements.txt
python src/gui.py
```


## 📦 Requirements

If you're running the app from source, install the required Python packages:

```
flet
```

These are listed in the `requirements.txt` file.

## Contributing

Feel free to fork this repository and submit a pull request. Contributions, improvements, and bug fixes are always welcome!

## License

This project is open-source and available under the MIT License.