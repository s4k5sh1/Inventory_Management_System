# Inventory Management System for Clothes Selling

## About

This project is designed to help organise and track the profits made from my vintage clothes selling side business. I built this system to keep track of clothing inventory, purchase details, retail prices, and selling prices. It allows me to add, update, and delete items, while also managing profit calculations.

As I continue adding new features, the system will be updated.

**Initial Timeline:** The first implementation of this project was developed from June 2024 to September 2024.

## Features
- Add, view, update, and delete clothing items.
- Track purchase price, retail price, selling price, and quantity.
- Keep a log of items sold and profits made.
- Auto-renumber IDs after deletion of items.

## Frameworks/Libraries Used

- **Python**: The core programming language used for all functionality.
- **SQLite**: For managing the database that stores inventory information.
- **Tkinter**: For building the graphical user interface (GUI), which mimics a terminal-like experience.
- **Git**: Version control for tracking project changes and pushing updates to GitHub.

## Setup Instructions

To set up and run the project on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/InventoryManagementSystem.git
    ```

2. **Navigate into the project directory**:
    ```bash
    cd InventoryManagementSystem
    ```

3. **Install the required dependencies** (Python is required):
    - Python 3.x should be installed on your machine.
    - Tkinter is part of the Python standard library, so no extra installation is required.

4. **Run the project**:
    - Open a terminal and run the following command to start the application:
    ```bash
    python gui.py
    ```

## How to Use
1. **Add Clothing Item**: Open the "Add Item" option in the GUI and input the details for a new clothing item.
2. **View Items**: View all the items added to the inventory.
3. **Update Clothing Item**: Select an item to update any of its details.
4. **Delete Item**: Remove an item from the inventory, and the IDs will be renumbered accordingly.

## Future Updates
- **Profit Reports**: Plan to add functionality for generating profit reports based on sales data.
- **Advanced Search**: Implement an advanced search feature to filter items by name, date, and price.
