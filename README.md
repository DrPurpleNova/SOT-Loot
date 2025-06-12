# Sea of Thieves Treasure Calculator GUI

This project is a graphical user interface (GUI) application for calculating treasure gains in the game Sea of Thieves. It allows users to interact with existing treasure calculation logic, select emissaries, set emissary levels, and view potential gold gains based on collected treasures.

## Project Structure

```
sotcalc-gui
├── src
│   ├── calc.py        # Contains the treasure calculation logic
│   ├── gui.py         # Implements the GUI for user interaction
│   └── __init__.py    # Marks the directory as a Python package
├── requirements.txt    # Lists the dependencies required for the project
└── README.md           # Documentation for the project
```

## Features

- **Searchable Treasure List**: Users can search for treasures in real-time as they type.
- **Emissary Selection**: Users can select an emissary from a dropdown list.
- **Emissary Level Setting**: Users can set the emissary level to calculate potential gains.
- **Real-time Calculation**: The application updates the minimum and maximum gold gain as users interact with the inputs.

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Running the Application

To start the application, run the following command in your terminal:

```
python src/gui.py
```

Make sure you have Python installed on your system. The application will open a window where you can interact with the treasure calculation features.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements or bug fixes are welcome!

## License

This project is open-source and available under the MIT License.