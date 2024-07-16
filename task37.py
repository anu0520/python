def nth_largest_number(nums, n):
    if n <= 0 or n > len(nums):
        return None  # Invalid input for N

    # Sort the list in descending order
    sorted_nums = sorted(nums, reverse=True)

    # Return the Nth largest number (index n-1 due to 0-indexing)
    return sorted_nums[n - 1]


def main():
    try:
        # Sample Input
        nums = [14, 67, 48, 23, 5, 62]
        print("List:", nums)

        # Input for Nth largest number
        n = int(input("N = "))

        # Calculate the Nth largest number
        result = nth_largest_number(nums, n)

        if result is not None:
            print(f"{n}th Largest number: {result}")
        else:
            print("Invalid input for N.")

    except ValueError:
        print("Invalid input for N. Please enter a valid integer.")


# Test cases
test_cases = [0, -5, 1, 'M', '%']

print("Test cases:")
for test in test_cases:
    print(f"N = {test}")
    main()
    print()
