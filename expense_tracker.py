# Global state variables
expense_list = []  # List of dictionaries
monthly_budget = 0.0
def validate_amount():
    """Ensures positive float input."""
    while True:
        try:
            amount = float(input("Enter Amount: "))
            if amount > 0:
                return amount
            else:
                print("Amount must be positive and greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
def add_expense():
    print("\n--- ADD EXPENSE ---")
    description = input("Enter Expense Description: ").strip()
    print("Categories: Food / Travel / Bills / Entertainment / Other")
    category = input("Enter Category: ").strip()
    amount = validate_amount()
    date = input("Enter Date (DD-MM-YYYY): ").strip()
    # Store record using a dictionary
    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }
    expense_list.append(expense)
    print("Expense added successfully!")
def view_expenses():
    print("\n========= EXPENSE LOG =========")
    if not expense_list:
        print("No expenses recorded yet.")
        return
    print(f"%-5s %-20s %-15s %-12s %-12s" % ("S.No", "Description", "Category", "Amount", "Date"))
    print("-" * 65)
    for i in range(len(expense_list)):
        exp = expense_list[i]
        print(f"%-5d %-20s %-15s Rs.%-9.2f %-12s" % (i + 1, exp["description"], exp["category"], exp["amount"], exp["date"]))
def category_summary():
    print("\n========= CATEGORY-WISE SUMMARY =========")
    if not expense_list:
        print("No expenses recorded yet.")
        return
    summary_dict = {}
    for exp in expense_list:
        cat = exp["category"]
        amt = exp["amount"]
        if cat in summary_dict:
            summary_dict[cat] += amt
        else:
            summary_dict[cat] = amt
    for cat, total in summary_dict.items():
        print(f"Category: {cat:15} | Total Spent: Rs. {total:.2f}")
def get_top_category():
    if not expense_list:
        return "None", 0.0
    summary_dict = {}
    for exp in expense_list:
        cat = exp["category"]
        amt = exp["amount"]
        if cat in summary_dict:
            summary_dict[cat] += amt
        else:
            summary_dict[cat] = amt
    top_cat = "None"
    max_amt = 0.0
    for cat, total in summary_dict.items():
        if total > max_amt:
            max_amt = total
            top_cat = cat
    return top_cat, max_amt
def budget_report():
    print("\n========= BUDGET REPORT =========")
    total_spent = 0.0
    for exp in expense_list:
        total_spent += exp["amount"]
    remaining = monthly_budget - total_spent
    if monthly_budget > 0:
        used_percentage = (total_spent / monthly_budget) * 100
    else:
        used_percentage = 0.0
    print(f"Total Spent   : Rs. {total_spent:.2f}")
    print(f"Budget Limit  : Rs. {monthly_budget:.2f}")
    print(f"Remaining     : Rs. {remaining:.2f}")
    print(f"Used          : {used_percentage:.2f}%")
    # Warning levels logic
    if used_percentage >= 100:
        print(" CRITICAL WARNING: You have exceeded 100% of your budget limit!")
    elif used_percentage >= 80:
        print(f" WARNING: You have used {used_percentage:.2f}% of your budget!")
    top_cat, top_amt = get_top_category()
    print(f"Top Category  : {top_cat} (Rs. {top_amt:.2f})")
# --- Main Menu Logic Loop (Prompting Budget at Start) ---
print("===== PERSONAL EXPENSE TRACKER =====")
try:
    monthly_budget = float(input("Set your Monthly Budget: Rs. "))
except ValueError:
    monthly_budget = 5000.0
    print("Invalid budget input. Defaulting budget to Rs. 5000.00")
while True:
    print("\n1. Add Expense")
    print("2. View All")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")
    choice = input("Choice: ").strip()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        budget_report()
    elif choice == "5":
        print("Exiting Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid Choice! Please enter 1-5.")