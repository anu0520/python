def calculate_grade(subjects):
    total = sum(subjects)
    aggregate = total / len(subjects)

    if aggregate > 75:
        grade = "DISTINCTION"
    elif aggregate >= 60:
        grade = "First Division"
    elif aggregate >= 50:
        grade = "Second Division"
    elif aggregate >= 40:
        grade = "Third Division"
    else:
        grade = "Fail"

    return total, aggregate, grade


def main():
    try:
        # Input marks for each subject
        marks = []
        subjects = ["Python", "C Programming", "Mathematics", "Physics"]

        for subject in subjects:
            mark = float(input(f"Enter the marks in {subject}: "))
            marks.append(mark)

        # Calculate total, aggregate and determine grade
        total, aggregate, grade = calculate_grade(marks)

        # Print results
        print(f"Total = {total}")
        print(f"Aggregate = {aggregate}")
        print(grade)

    except ValueError:
        print("Invalid input. Please enter numeric values for marks.")


# Test cases
test_cases = [
    [18, 76, 93, 65],
    [73, 78, 79, 75],
    [98, 106, 120, 95],
    [96, 73, -85, 95],
    [78, 59.8, 76, 79]
]

for marks in test_cases:
    print(f"Sample Input & Output:")
    print(f"Enter the marks in Python: {marks[0]}")
    print(f"Enter the marks in C Programming: {marks[1]}")
    print(f"Enter the marks in Mathematics: {marks[2]}")
    print(f"Enter the marks in Physics: {marks[3]}")
    main()
    print()
