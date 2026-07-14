# Master Dictionary: ISBN -> {title, author, available, borrower, student_id, issue_date}
library_catalog = {
    "978-3-16-148410-0": {"title": "Python Programming", "author": "John Smith", "available": True, 
                          "borrower": None, "student_id": None, "issue_date": None}
    }
def check_due_date():
    return "28-June-2026"
def add_book():
    print("\n====== Add Book ======")
    isbn = input("Enter ISBN : ")
    if isbn in library_catalog:
        print("Error: Book with this ISBN already exists.")
        return
    title = input("Enter Title : ")
    author = input("Enter Author : ")
    library_catalog[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None,
        "student_id": None,
        "issue_date": None
    }
    print("Book Registered Successfully!")
def issue_book():
    """Issue a book to a student."""
    print("\n====== Issue Book ======")
    isbn = input("Enter ISBN : ")
    if isbn not in library_catalog:
        print("Error: Book not found.")
        return
    book = library_catalog[isbn]
    if not book["available"]:
        print("Error: Book is already issued.")
        return
    student_id = input("Enter Borrower ID : ")
    borrower_name = input("Enter Your Name : ")
    # Update state tracking
    book["available"] = False
    book["borrower"] = borrower_name
    book["student_id"] = student_id
    book["issue_date"] = "21-June-2026"
    print("\nBook Issued Successfully!")
    print(f"Title : {book['title']}")
    print(f"Due Date: {check_due_date()}")
def return_book():
    print("\n====== Return Book ======")
    isbn = input("Enter ISBN : ").strip()
    if isbn not in library_catalog:
        print("Error: Book not found.")
        return
    book = library_catalog[isbn]
    if book["available"]:
        print("Error: Book was not issued.")
        return
    # Reset state tracking
    book["available"] = True
    book["borrower"] = None
    book["student_id"] = None
    book["issue_date"] = None
    print("Return confirmation and updated status successfully!")
def search_book():
    print("\n====== Search Book ======")
    keyword = input("Enter search keyword: ").lower()
    found = False
    for isbn, details in library_catalog.items():
        if keyword in details["title"].lower() or keyword in details["author"].lower():
            status = "Available" if details["available"] else "Issued"
            print(f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | Status: {status}")
            found = True
    if not found:
        print("No matching books found.")
def view_catalog():
    print("\n====== View All ======")
    if not library_catalog:
        print("Catalog is empty.")
        return
    for isbn, details in library_catalog.items():
        status = "Available" if details["available"] else f"Issued to {details['borrower']}"
        print(f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | Status: {status}")
# --- Menu Logic to execute your functions ---
while True:
    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All")
    print("6. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        view_catalog()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid Choice!")