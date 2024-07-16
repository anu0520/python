def remove_duplicates_sorted_array(arr):
    if not arr:
        return []

    # Initialize an empty list to store unique elements
    unique_elements = []
    previous_element = None

    # Iterate through the array and collect unique elements
    for num in arr:
        if num != previous_element:
            unique_elements.append(num)
            previous_element = num

    return unique_elements


def main():
    try:
        # Sample Input
        arr = [15, 14, 25, 14, 32, 14, 31]
        print("Array:", arr)

        # Remove duplicates
        unique_array = remove_duplicates_sorted_array(arr)

        # Sample Output
        print("Sorted Array without duplicates:", unique_array)

    except ValueError:
        print("Invalid input. Please enter valid integers in the array.")


# Test cases
test_cases = [
    [16, 16, 16, 16, 16],
    [0, 0, 0, 0],
    [-12, -78, -35, -42],
    [1, 2, 3, 7, 8, 9, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]
]

print("Test cases:")
for i, test_case in enumerate(test_cases):
    print(f"{i + 1}. Array:", test_case)
    unique_array = remove_duplicates_sorted_array(test_case)
    print("Sorted Array without duplicates:", unique_array)
    print()
