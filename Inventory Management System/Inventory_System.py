import json
import os

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {}

# Function to save inventory data to file
def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

# Function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1. Add new Product")
    print("2. Update Product Information")
    print("3. Display Product items ")
    print("4. Exit")

# Function to add a new product to the inventory
def add_product(inventory):
    print("\nAdding Product:")
    product_id = input("Enter Product ID: ")
    if product_id in inventory:
        print("Error: Product ID already exists.")
        return

    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity: ")

    inventory[product_id] = {
        "Product Name": product_name,
        "Category": category,
        "Price": float(price),
        "Quantity": int(quantity)
    }
    print("Product added successfully.")

# Function to update existing product information
def update_product(inventory):
    print("\nUpdating Product Information:")
    product_id = input("Enter Product ID to update: ")
    if product_id not in inventory:
        print("Error: Product ID does not exist.")
        return

    print("Select attribute to update:")
    print("1. Product Name")
    print("2. Category")
    print("3. Price")
    print("4. Quantity")
    choice = input("Enter your choice: ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        return

    if choice == "1":
        inventory[product_id]["Product Name"] = input("Enter new Product Name: ")
    elif choice == "2":
        inventory[product_id]["Category"] = input("Enter new Category: ")
    elif choice == "3":
        new_price = input("Enter new Price: ")
        if not (new_price.isdigit() or new_price.replace('.', '', 1).isdigit()):
            print("Error: Price should be a numeric value.")
            return
        inventory[product_id]["Price"] = float(new_price)
    elif choice == "4":
        new_quantity = input("Enter new Quantity: ")
        if not new_quantity.isdigit():
            print("Error: Quantity should be a numeric value.")
            return
        inventory[product_id]["Quantity"] = int(new_quantity)

    print("Product updated successfully.")

# Function to display inventory status
def display_inventory(inventory):
    print("\nInventory:")
    print("{:<15} {:<20} {:<15} {:<10} {:<10}".format("Product ID", "Product Name", "Category", "Price", "Quantity"))
    for product_id, product_info in sorted(inventory.items()):
        print("{:<15} {:<20} {:<15} ${:<9.2f} {:<10}".format(product_id, product_info["Product Name"],
                                                            product_info["Category"], product_info["Price"],
                                                            product_info["Quantity"]))

# Main function
def main():
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            update_product(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "4":
            save_inventory(inventory)
            print("Inventory saved successfully. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
