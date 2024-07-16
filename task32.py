def calculate_users(total_users, staff_users):
    if total_users <= 0 or staff_users < 0:
        print("Invalid input. Please enter valid numbers.")
        return

    # Calculate non-teaching staff users
    non_teaching_staff_users = staff_users // 3

    # Calculate student users
    student_users = total_users - staff_users - non_teaching_staff_users

    # Print results
    print(f"Student Users: {student_users}")


# Test cases
test_cases = [
    (0, 0),
    (-143, 0),
    (1026, 1026),
    (450, 540),
    (600, 450)
]

for total_users, staff_users in test_cases:
    print(f"Total Users: {total_users}, Staff Users: {staff_users}")
    calculate_users(total_users, staff_users)
    print()
