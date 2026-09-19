def show_students(**students):
    """Display student names and their subjects using nested loops."""
    for student, subjects in students.items():
        print(f"{student}:")
        for subject in subjects:
            print(f"  - {subject}")


show_students(
    YasH=["Python", "LeetCode", "GitHub"],
    Alex=["Java", "SQL", "Git"],
)
