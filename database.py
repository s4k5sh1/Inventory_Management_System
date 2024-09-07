import sqlite3

# Function to connect to the SQLite database
def connect_db():
    """Connect to the database and return the connection object."""
    connection = sqlite3.connect('database.db')
    return connection

# Function to create the 'clothes' table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS clothes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        purchase_price REAL NOT NULL,
                        quantity INTEGER NOT NULL,
                        purchase_date TEXT NOT NULL,
                        retail_price REAL,
                        selling_price REAL
                    )''')
    
    conn.commit()
    conn.close()

# Function to add a clothing item
def add_clothing(name, purchase_price, quantity, purchase_date, retail_price=None, selling_price=None):
    conn = connect_db()  # Call the function to get the connection object
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO clothes (name, purchase_price, quantity, purchase_date, retail_price, selling_price)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, purchase_price, quantity, purchase_date, retail_price, selling_price))
    
    conn.commit()
    conn.close()

# Function to view all clothing items
def view_clothes():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM clothes')
    clothes = cursor.fetchall()
    
    conn.close()
    return clothes

# Function to update a clothing item
def update_clothing(clothing_id, name=None, purchase_price=None, quantity=None, purchase_date=None, retail_price=None, selling_price=None):
    conn = connect_db()
    cursor = conn.cursor()

    if name:
        cursor.execute('UPDATE clothes SET name = ? WHERE id = ?', (name, clothing_id))
    if purchase_price:
        cursor.execute('UPDATE clothes SET purchase_price = ? WHERE id = ?', (purchase_price, clothing_id))
    if quantity:
        cursor.execute('UPDATE clothes SET quantity = ? WHERE id = ?', (quantity, clothing_id))
    if purchase_date:
        cursor.execute('UPDATE clothes SET purchase_date = ? WHERE id = ?', (purchase_date, clothing_id))
    if retail_price:
        cursor.execute('UPDATE clothes SET retail_price = ? WHERE id = ?', (retail_price, clothing_id))
    if selling_price:
        cursor.execute('UPDATE clothes SET selling_price = ? WHERE id = ?', (selling_price, clothing_id))
    
    conn.commit()
    conn.close()

# Function to delete a clothing item
def delete_clothing(clothing_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Delete the clothing item
    cursor.execute('DELETE FROM clothes WHERE id = ?', (clothing_id,))
    
    # Check if the table is empty
    cursor.execute('SELECT COUNT(*) FROM clothes')
    count = cursor.fetchone()[0]

    if count == 0:
        # If the table is empty, reset the AUTOINCREMENT for the 'id' column
        cursor.execute('DELETE FROM sqlite_sequence WHERE name="clothes";')
    else:
        # Renumber the IDs if the table is not empty
        cursor.execute('SELECT id FROM clothes ORDER BY id')
        rows = cursor.fetchall()

        new_id = 1
        for row in rows:
            current_id = row[0]
            cursor.execute('UPDATE clothes SET id = ? WHERE id = ?', (new_id, current_id))
            new_id += 1

    conn.commit()
    conn.close()

















               

               




