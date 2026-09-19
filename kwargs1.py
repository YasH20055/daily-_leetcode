def show_student_details(**students):
    """Display each student's subjects using nested loops."""
    for student, details in students.items():
        print(f"{student}:")
        for key, value in details.items():
            print(f"  {key}: {value}")


show_student_details(
    YasH={"age": 21, "subjects": ["Python", "LeetCode"]},
    Alex={"age": 22, "subjects": ["Java", "SQL"]},
)
