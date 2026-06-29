import random

def load_questions():
    return [
        ("Which data type is IMMUTABLE in Python?", "List", "Dictionary", "Tuple", "Set", "C"),
        ("What is the correct file extension for Python files?", ".pyt", ".py", ".pyw", ".python", "B"),
        ("Which keyword is used to create a function in Python?", "fun", "function", "def", "lambda", "C"),
        ("What is the output of len(['apple', 'banana', 'cherry'])?", "3", "1", "2", "6", "A"),
        ("Which of the following method removes the last element from a list?", "remove()", "pop()", "delete()", "discard()", "B"),
        ("How do you start a comment in Python?", "//", "/*", "#", "--", "C"),
        ("Which collection does NOT allow duplicate members?", "List", "Tuple", "Set", "Dictionary Values", "C"),
        ("Which statement is used to stop a loop prematurely?", "exit", "break", "continue", "stop", "B"),
        ("What is the correct way to import a module named 'math'?", "import math", "include math", "using math", "require math", "A"),
        ("Which block handles exceptions in Python?", "catch", "try", "except", "error", "C")
    ]
def display_question(q_num, q_tuple):
    """Displays a question with options"""
    print(f"\nQ{q_num}: {q_tuple[0]}")
    print(f" A. {q_tuple[1]}   B. {q_tuple[2]}")
    print(f" C. {q_tuple[3]}   D. {q_tuple[4]}")
def get_answer():
    """Accepts and validates student answer"""
    while True:
        ans = input("Your Answer (A/B/C/D): ").strip().upper()
        if ans in ['A', 'B', 'C', 'D']:
            return ans
        print("Invalid option! Please enter A, B, C, or D.")
def calculate_grade(percentage):
    """Returns grade from percentage"""
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "B+"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "F"
def show_wrong_answers(wrong_answers):
    """Displays incorrectly answered questions"""
    print("\n====== WRONG ANSWERS REVIEW ======")
    for item in wrong_answers:
        print(f"\nQuestion: {item[0]}")
        print(f"Your Answer: {item[1]}")
        print(f"Correct Answer: {item[2]}")
def show_report(report):
    """Prints final formatted result report"""
    print("\n====== RESULT REPORT ======")
    print(f"Name    : {report['name']}")
    print(f"Score   : {report['score']} / {report['total']}")
    print(f"Percent : {report['percentage']:.2f}%")
    print(f"Grade   : {report['grade']}")
    print(f"Result  : {report['result']}")
def evaluate_quiz():
    """Scores all answers and compiles result"""
    print("===== PYTHON QUIZ SYSTEM =====")
    name = input("Enter Student Name: ").strip()
    roll = input("Enter Roll Number: ").strip()
    questions = load_questions()
    random.shuffle(questions)
    score = 0
    wrong_answers = []
    for idx, q in enumerate(questions, 1):
        display_question(idx, q)
        ans = get_answer()
        if ans == q[5]:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect!")
            wrong_answers.append((q[0], ans, q[5]))
    total = len(questions)
    percentage = (score / total) * 100
    grade = calculate_grade(percentage)
    verdict = "PASS" if percentage >= 50 else "FAIL"
    result_report = {
        "name": f"{name} | Roll: {roll}",
        "score": score,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": verdict
    }
    show_report(result_report)
    if wrong_answers:
        show_wrong_answers(wrong_answers)
# Run the system
evaluate_quiz()