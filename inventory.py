from database import create_table, add_clothing, view_clothes, delete_clothing, update_clothing

create_table()

def add_item_to_inventory(name, purchase_price, quantity, purchase_date, retail_price=None, selling_price=None):
    add_clothing(name, purchase_price, quantity, purchase_date, retail_price, selling_price)

def get_all_items():
    return view_clothes()

def remove_item_from_inventory(clothing_id):
    delete_clothing(clothing_id)


def update_item_in_inventory(clothing_id, name=None, purchase_price=None, quantity=None, purchase_date=None, retail_price=None, selling_price=None):
    update_clothing(clothing_id, name, purchase_price, quantity, purchase_date, retail_price, selling_price)
