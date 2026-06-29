student_details = {}
def calculate_grade(percentage):
    """Returns a letter grade based on the calculated percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"
def add_student():
    print("\n--- Add New Student ---")
        # 1. Validate Roll Number and check for duplicates
    while True:
        roll_no = input("Enter Roll Number: ")
        if not roll_no:
            print("Error: Roll number cannot be empty.")
            continue
        if roll_no in student_details:
            print(f"Error: A student with Roll Number '{roll_no}' already exists!")
            return
        break
    # 2. Collect Student Name
    name = input("Enter Student Name: ")
    while not name:
        print("Error: Name cannot be empty.")
        name = input("Enter Student Name: ")
    # 3. Collect and Validate Marks for 5 Subjects using try-except
    marks = []
    print("Enter marks for 5 subjects (out of 100):")
    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"  Subject {i} Marks: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("  Error: Marks must be between 0 and 100.")
            except ValueError:
                print("  Error: Please enter a valid number.")
    # 4. calculations
    total_marks = sum(marks)
    percentage = total_marks / 5
    grade = calculate_grade(percentage)
    # 5. Store record in the nested dictionary 
    student_details[roll_no] = {"name": name,"marks": marks,"percentage": percentage,"grade": grade}
    print("\n=== Record Added Successfully ===")
    print(f"Name: {name} | Roll: {roll_no} | %: {percentage:.2f} | Grade: {grade}")
def view_all():
    print("\n========================= ALL STUDENT RECORDS ==========================")
    if not student_details:
        print("The database is currently empty. No records to display.")
        print("========================================================================")
        return
    print(f"{'Roll No':<10} | {'Name':<20} | {'Percentage':<12} | {'Grade':<6}")
    print("-" * 60)
    for roll_no, data in student_details.items():
        print(f"{roll_no:<10} | {data['name']:<20} | {data['percentage']:<12.2f} | {data['grade']:<6}")
    print("========================================================================")
def search_student():
    print("\n--- Search Student ---")
    roll_no = input("Enter Roll Number to search: ")
    student = student_details.get(roll_no)
    if student:
        print("\n=== Student Profile Found ===")
        print(f"Roll Number : {roll_no}")
        print(f"Name        : {student['name']}")
        print(f"Subject Marks: {student['marks']}")
        print(f"Percentage  : {student['percentage']:.2f}%")
        print(f"Final Grade : {student['grade']}")
    else:
        print("Error: Student record not found.")
def update_student():
    print("\n--- Update Student Record ---")
    roll_no = input("Enter Roll Number to update: ")
    if roll_no not in student_details:
        print("Error: Student record not found.")
        return
    student = student_details[roll_no]
    print(f"Updating record for {student['name']} (Roll: {roll_no})")
    print("Leave input blank and press enter to keep the current value.\n")
    # Update Name
    new_name = input(f"Enter new Name [{student['name']}]: ")
    if new_name:
        student['name'] = new_name
    # Update Marks
    update_marks_choice = input("Do you want to update subject marks? (yes/no): ").lower()
    if update_marks_choice == 'yes':
        new_marks = []
        for i in range(1, 6):
            while True:
                try:
                    mark = float(input(f"  New Subject {i} Marks [{student['marks'][i-1]}]: "))
                    if 0 <= mark <= 100:
                        new_marks.append(mark)
                        break
                    else:
                        print("  Error: Marks must be between 0 and 100.")
                except ValueError:
                    print("  Error: Invalid format. Re-enter number.")
        # Recalculate metrics if marks change
        student['marks'] = new_marks
        student['percentage'] = sum(new_marks) / 5
        student['grade'] = calculate_grade(student['percentage'])
    print("\n=== Record Updated Successfully ===")
def delete_student():
    print("\n--- Delete Student Record ---")
    roll_no = input("Enter Roll Number to delete: ").strip()
    if roll_no in student_details:
        confirm = input(f"Are you sure you want to delete {student_details[roll_no]['name']}'s record? (yes/no): ").strip().lower()
        if confirm == 'yes':
            removed_student = student_details.pop(roll_no)
            print(f"Success: Record for '{removed_student['name']}' has been permanently deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Error: Student record not found.")
def show_menu():
    print("\n====== STUDENT MANAGEMENT SYSTEM ======")
    print("1. Add Student    2. View All")
    print("3. Search         4. Update")
    print("5. Delete         6. Exit")
    print("=======================================")
    while True:
        try:
            choice = int(input("Enter choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Error: Selection out of bounds. Enter an option from 1 to 6.")
        except ValueError:
            print("Error: Invalid entry format. Please enter an integer value.")
def main():
    """Main execution loop driver."""
    while True:
        choice = show_menu()
        if choice == 1:
            add_student()
        elif choice == 2:
            view_all()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("\nExiting Student Management System. Goodbye!")
            break

if __name__ == "__main__":
    main()