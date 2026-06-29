import os
# Global transaction log to keep track of stock movements during the session
transaction_log = []
def load_inventory():
    inventory = {}
    filename = "inventory.txt"
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    p_id, name, category, price, qty, reorder = line.split(",")
                    inventory[p_id] = {
                        "name": name,
                        "category": category,
                        "price": float(price),
                        "quantity": int(qty),
                        "reorder_level": int(reorder)
                    }
            return inventory
        except Exception:
            print("Error reading file. Loading pre-populated products.")
    return {
        "P001": {"name": "Laptop", "category": "Electronics", "price": 58000.0, "quantity": 5, "reorder_level": 3},
        "P002": {"name": "Smartphone", "category": "Electronics", "price": 25000.0, "quantity": 8, "reorder_level": 4},
        "P003": {"name": "Wireless Mouse", "category": "Electronics", "price": 1200.0, "quantity": 2, "reorder_level": 5},
        "P004": {"name": "T-Shirt", "category": "Apparel", "price": 799.0, "quantity": 15, "reorder_level": 5},
        "P005": {"name": "Jeans", "category": "Apparel", "price": 1499.0, "quantity": 12, "reorder_level": 4},
        "P006": {"name": "Notebook", "category": "Stationery", "price": 60.0, "quantity": 50, "reorder_level": 10},
        "P007": {"name": "Gel Pen", "category": "Stationery", "price": 20.0, "quantity": 8, "reorder_level": 15},
        "P008": {"name": "Backpack", "category": "Apparel", "price": 2100.0, "quantity": 6, "reorder_level": 2}
    }
def save_inventory(inventory):
    """Write data to inventory.txt."""
    try:
        with open("inventory.txt", "w") as f:
            for p_id, info in inventory.items():
                line = f"{p_id},{info['name']},{info['category']},{info['price']},{info['quantity']},{info['reorder_level']}\n"
                f.write(line)
        print("Inventory saved to inventory.txt successfully.")
    except Exception as e:
        print(f" Failed to save inventory: {e}")
def log_transaction(p_id, tx_type, qty):
    """Append entry to transaction history log."""
    transaction_log.append(f"Type: {tx_type.upper()} | Product ID: {p_id} | Quantity: {qty}")
def add_product(inventory):
    """Register new product."""
    print("\n--- ADD NEW PRODUCT ---")
    p_id = input("Enter Product ID: ").strip().upper()
    if p_id in inventory:
        print(" Error: Product ID already exists!")
        return
    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    try:
        price = float(input("Enter Unit Price: "))
        qty = int(input("Enter Initial Quantity: "))
        reorder = int(input("Enter Reorder Level: "))
        inventory[p_id] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": qty,
            "reorder_level": reorder
        }
        print(f"Product '{name}' added successfully.")
    except ValueError:
        print(" Invalid numeric input!")
def stock_in(inventory):
    """Add quantity to existing product."""
    print("\n--- STOCK-IN (RESTOCK) ---")
    p_id = input("Enter Product ID: ").strip().upper()
    if p_id not in inventory:
        print("Product ID not found.")
        return
    try:
        qty = int(input(f"Enter quantity to add: "))
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return
        inventory[p_id]["quantity"] += qty
        log_transaction(p_id, "IN", qty)
        print(f"Stock updated. New Quantity: {inventory[p_id]['quantity']}")
    except ValueError:
        print(" Invalid number.")
def stock_out(inventory):
    """Deduct quantity with validation."""
    print("\n--- STOCK-OUT (SALE) ---")
    p_id = input("Enter Product ID: ").strip().upper()
    
    if p_id not in inventory:
        print("Product ID not found.")
        return
    try:
        qty = int(input(f"Enter quantity to deduct: "))
        if qty <= 0:
            print("Quantity must be greater than zero.")
            return
        if inventory[p_id]["quantity"] >= qty:
            inventory[p_id]["quantity"] -= qty
            log_transaction(p_id, "OUT", qty)
            print(f"Transaction complete. Remaining Stock: {inventory[p_id]['quantity']}")
        else:
            print(f" Error: Insufficient stock! Available: {inventory[p_id]['quantity']}.")
    except ValueError:
        print("Invalid number.")
def get_total_value(inventory):
    """Returns total inventory valuation."""
    total_val = 0.0
    for info in inventory.values():
        total_val += info["price"] * info["quantity"]
    return total_val
def view_inventory(inventory):
    """Display full formatted table."""
    print("\n" + "="*70)
    print(f"{'ID':<6} {'Product Name':<18} {'Category':<15} {'Price':<10} {'Qty':<6} {'Reorder':<8}")
    print("="*70)
    for p_id, info in inventory.items():
        print(f"{p_id:<6} {info['name']:<18} {info['category']:<15} Rs.{info['price']:<7.2f} {info['quantity']:<6} {info['reorder_level']:<8}")
    print("="*70)
    print(f"Total Valuation: Rs. {get_total_value(inventory):,.2f}")
def low_stock_alert(inventory):
    """List products below reorder level."""
    print("\n======= LOW-STOCK ALERT =======")
    for p_id, info in inventory.items():
        if info["quantity"] <= info["reorder_level"]:
            print(f" ID: {p_id} | Name: {info['name']} | Stock: {info['quantity']} (Reorder: {info['reorder_level']})")
def generate_report(inventory):
    """Summary statistics and analytics."""
    print("\n======= INVENTORY REPORT =======")
    total_products = len(inventory)
    total_value = get_total_value(inventory)
    categories_set = set(info["category"] for info in inventory.values())
    categories_str = ", ".join(categories_set)
    low_stock_count = sum(1 for info in inventory.values() if info["quantity"] <= info["reorder_level"])
    highest_value_item = ""
    max_value = -1.0
    for info in inventory.values():
        item_val = info["price"] * info["quantity"]
        if item_val > max_value:
            max_value = item_val
            highest_value_item = f"{info['name']} (Rs. {info['price']:,} x {info['quantity']} = Rs. {item_val:,.2f})"
    print(f"Total Products : {total_products}")
    print(f"Total Stock Value : Rs. {total_value:,.2f}")
    print(f"Categories : {categories_str}")
    print(f"Low Stock Items : {low_stock_count}")
    print(f"Highest Value Item: {highest_value_item}")
    print("\n--- Transaction Log ---")
    for log in transaction_log:
        print(log)
def main():
    """Main execution loop framework."""
    inventory = load_inventory()
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product\n2. Stock-In\n3. Stock-Out\n4. View Inventory\n5. Low Stock Alert\n6. Report\n7. Save & Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            stock_in(inventory)
        elif choice == "3":
            stock_out(inventory)
        elif choice == "4":
            view_inventory(inventory)
        elif choice == "5":
            low_stock_alert(inventory)
        elif choice == "6":
            generate_report(inventory)
        elif choice == "7":
            save_inventory(inventory)
            print("EXIT.")
            break
        else:
            print("Invalid choice.")
# Direct execution call
main()