def show_student_subjects(**students):
    """Display each student's subjects using nested loops."""
    for student, subjects in students.items():
        print(f"{student}:")
        for subject in subjects:
            print(f"  - {subject}")


show_student_subjects(
    YasH=["Python", "LeetCode", "GitHub"],
    Alex=["Java", "SQL", "Git"],
)
