import tkinter as tk
from tkinter import messagebox
from inventory import add_item_to_inventory, get_all_items, remove_item_from_inventory, update_item_in_inventory


root = tk.Tk()
root.title("Inventory Management System")
root.geometry("800x400")  
root.config(bg="#000000")  
monospaced_font = ("Menlo", 12)  

title_label = tk.Label(root, text="Clothing Inventory Terminal", font=("Menlo", 16), bg="#000000", fg="white")
title_label.pack(pady=10)


frame = tk.Frame(root, bg="#000000")
frame.pack(pady=10)


def display_terminal_output(output):
    output_textbox.delete(1.0, tk.END)  # Clear previous content
    output_textbox.insert(tk.END, output)  # Insert new content
    output_textbox.see(tk.END)  # Scroll to the end


output_textbox = tk.Text(root, height=15, width=100, font=monospaced_font, bg="#000000", fg="#c0c0c0", bd=0)
output_textbox.pack(pady=5)


def add_item():
    add_window = tk.Toplevel(root)
    add_window.title("Add Clothing Item")
    add_window.geometry("400x300")
    add_window.config(bg="#000000")

    tk.Label(add_window, text="Name", font=monospaced_font, bg="#000000", fg="white").grid(row=0, column=0)
    name_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Purchase Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=1, column=0)
    purchase_price_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    purchase_price_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Quantity", font=monospaced_font, bg="#000000", fg="white").grid(row=2, column=0)
    quantity_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    quantity_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Purchase Date (YYYY-MM-DD)", font=monospaced_font, bg="#000000", fg="white").grid(row=3, column=0)
    purchase_date_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    purchase_date_entry.grid(row=3, column=1)

    tk.Label(add_window, text="Retail Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=4, column=0)
    retail_price_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    retail_price_entry.grid(row=4, column=1)

    tk.Label(add_window, text="Selling Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=5, column=0)
    selling_price_entry = tk.Entry(add_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    selling_price_entry.grid(row=5, column=1)

    def submit_add_item():
        name = name_entry.get()
        purchase_price = float(purchase_price_entry.get())
        quantity = int(quantity_entry.get())
        purchase_date = purchase_date_entry.get()
        retail_price = float(retail_price_entry.get() or 0)
        selling_price = float(selling_price_entry.get() or 0)

        add_item_to_inventory(name, purchase_price, quantity, purchase_date, retail_price, selling_price)
        messagebox.showinfo("Success", "Clothing item added successfully!")
        add_window.destroy()
        display_terminal_output(f"Added item: {name}, Price: £{purchase_price:.2f}, Quantity: {quantity}\n")

    tk.Button(add_window, text="Add Item", font=monospaced_font, bg="#000000", fg="white", 
              highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat",
              command=submit_add_item).grid(row=6, column=0, columnspan=2)


add_button = tk.Button(frame, text="Add Clothing Item", font=monospaced_font, bg="#000000", fg="white", 
                       highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat", command=add_item)
add_button.grid(row=0, column=0, padx=10)


def view_items():
    clothes = get_all_items()
    output = "ID   Name         Purchase Price   Quantity   Purchase Date   Retail Price   Selling Price\n"
    output += "-"*90 + "\n"
    for item in clothes:
        output += f"{item[0]:<4} {item[1]:<18} £{item[2]:<14.2f} {item[3]:<9} {item[4]:<14} £{item[5]:<12.2f} £{item[6]:<12.2f}\n"
    display_terminal_output(output)


view_button = tk.Button(frame, text="View All Clothing Items", font=monospaced_font, bg="#000000", fg="white", 
                        highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat", command=view_items)
view_button.grid(row=0, column=1, padx=10)

# Function to update a clothing item
def update_item():
    update_window = tk.Toplevel(root)
    update_window.title("Update Clothing Item")
    update_window.geometry("400x300")
    update_window.config(bg="#000000")

    tk.Label(update_window, text="Clothing ID", font=monospaced_font, bg="#000000", fg="white").grid(row=0, column=0)
    clothing_id_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    clothing_id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Name", font=monospaced_font, bg="#000000", fg="white").grid(row=1, column=0)
    name_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    name_entry.grid(row=1, column=1)

    tk.Label(update_window, text="Purchase Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=2, column=0)
    purchase_price_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    purchase_price_entry.grid(row=2, column=1)

    tk.Label(update_window, text="Quantity", font=monospaced_font, bg="#000000", fg="white").grid(row=3, column=0)
    quantity_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    quantity_entry.grid(row=3, column=1)

    tk.Label(update_window, text="Purchase Date (YYYY-MM-DD)", font=monospaced_font, bg="#000000", fg="white").grid(row=4, column=0)
    purchase_date_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    purchase_date_entry.grid(row=4, column=1)

    tk.Label(update_window, text="Retail Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=5, column=0)
    retail_price_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    retail_price_entry.grid(row=5, column=1)

    tk.Label(update_window, text="Selling Price (£)", font=monospaced_font, bg="#000000", fg="white").grid(row=6, column=0)
    selling_price_entry = tk.Entry(update_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    selling_price_entry.grid(row=6, column=1)

    def submit_update_item():
        clothing_id = int(clothing_id_entry.get())
        name = name_entry.get() if name_entry.get() != "" else None
        purchase_price = float(purchase_price_entry.get()) if purchase_price_entry.get() != "" else None
        quantity = int(quantity_entry.get()) if quantity_entry.get() != "" else None
        purchase_date = purchase_date_entry.get() if purchase_date_entry.get() != "" else None
        retail_price = float(retail_price_entry.get()) if retail_price_entry.get() != "" else None
        selling_price = float(selling_price_entry.get()) if selling_price_entry.get() != "" else None

        update_item_in_inventory(clothing_id, name, purchase_price, quantity, purchase_date, retail_price, selling_price)
        messagebox.showinfo("Success", "Clothing item updated successfully!")
        update_window.destroy()

    tk.Button(update_window, text="Update Item", font=monospaced_font, bg="#000000", fg="white", 
              highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat",
              command=submit_update_item).grid(row=7, column=0, columnspan=2)


update_button = tk.Button(frame, text="Update Clothing Item", font=monospaced_font, bg="#000000", fg="white", 
                          highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat", command=update_item)
update_button.grid(row=0, column=3, padx=10)

def delete_item():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Clothing Item")
    delete_window.geometry("300x200")
    delete_window.config(bg="#000000")

    tk.Label(delete_window, text="Enter ID to delete", font=monospaced_font, bg="#000000", fg="white").grid(row=0, column=0)
    delete_entry = tk.Entry(delete_window, font=monospaced_font, bg="#000000", fg="white", insertbackground="white")
    delete_entry.grid(row=0, column=1)

    def submit_delete_item():
        clothing_id = int(delete_entry.get())
        remove_item_from_inventory(clothing_id)
        messagebox.showinfo("Success", "Clothing item deleted successfully!")
        delete_window.destroy()
        display_terminal_output(f"Deleted item with ID: {clothing_id}\n")

    tk.Button(delete_window, text="Delete", font=monospaced_font, bg="#000000", fg="white", 
              highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat", 
              command=submit_delete_item).grid(row=1, column=0, columnspan=2)


delete_button = tk.Button(frame, text="Delete Clothing Item", font=monospaced_font, bg="#000000", fg="white", 
                          highlightthickness=0, activebackground="#000000", activeforeground="white", relief="flat", command=delete_item)
delete_button.grid(row=0, column=2, padx=10)

root.mainloop()

