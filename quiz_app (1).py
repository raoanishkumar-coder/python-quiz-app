"""
Simple Python Quiz Application
------------------------------
- Presents 10 multiple-choice questions on basic Python, one by one
- Collects the user's answer for each question
- Evaluates responses internally
- Displays the final score only after the quiz is complete
"""


def run_quiz():
    # Each question: text, options (A-D), and correct option letter
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": {"A": "func", "B": "define", "C": "def", "D": "function"},
            "answer": "C",
        },
        {
            "question": "Which data type is used to store True/False values in Python?",
            "options": {"A": "int", "B": "bool", "C": "str", "D": "float"},
            "answer": "B",
        },
        {
            "question": "What is the output of: len('Python')?",
            "options": {"A": "5", "B": "6", "C": "7", "D": "Error"},
            "answer": "B",
        },
        {
            "question": "Which symbol is used for single-line comments in Python?",
            "options": {"A": "//", "B": "#", "C": "/* */", "D": "--"},
            "answer": "B",
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": {"A": "tuple", "B": "string", "C": "list", "D": "int"},
            "answer": "C",
        },
        {
            "question": "What is the output of: print(2 ** 3)?",
            "options": {"A": "5", "B": "6", "C": "8", "D": "9"},
            "answer": "C",
        },
        {
            "question": "Which function is used to take input from the user in Python?",
            "options": {"A": "scan()", "B": "input()", "C": "read()", "D": "get()"},
            "answer": "B",
        },
        {
            "question": "Which of the following is the correct file extension for Python files?",
            "options": {"A": ".pyt", "B": ".pt", "C": ".py", "D": ".python"},
            "answer": "C",
        },
        {
            "question": "What does the 'len()' function do?",
            "options": {
                "A": "Returns the largest item",
                "B": "Returns the length of an object",
                "C": "Returns the smallest item",
                "D": "Returns the type of an object",
            },
            "answer": "B",
        },
        {
            "question": "Which operator is used for floor division in Python?",
            "options": {"A": "/", "B": "//", "C": "%", "D": "**"},
            "answer": "B",
        },
    ]

    print("=" * 50)
    print("       WELCOME TO THE PYTHON QUIZ APP")
    print("=" * 50)
    print(f"Total Questions: {len(questions)}")
    print("Choose A, B, C, or D for each question.\n")

    user_answers = []  # store responses internally

    # Loop through each question one by one
    for index, q in enumerate(questions, start=1):
        print(f"Q{index}. {q['question']}")
        for option, text in q["options"].items():
            print(f"   {option}. {text}")

        # Keep asking until a valid option is entered
        while True:
            choice = input("Your answer (A/B/C/D): ").strip().upper()
            if choice in q["options"]:
                user_answers.append(choice)
                break
            else:
                print("Invalid choice. Please enter A, B, C, or D.")
        print()  # blank line between questions

    # Evaluate answers AFTER the quiz is complete
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    # Show final score only at the end
    print("=" * 50)
    print("              QUIZ COMPLETED")
    print("=" * 50)
    print(f"Your Final Score: {score} / {len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent! Perfect score.")
    elif percentage >= 60:
        print("Good job! Keep practicing.")
    else:
        print("Keep learning. You'll do better next time.")
    print("=" * 50)


if __name__ == "__main__":
    run_quiz()
