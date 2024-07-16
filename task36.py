def factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1  # Base case: factorial of 0 and 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!


def main():
    try:
        n = int(input("Enter the value of n: "))

        if n < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = factorial(n)
            if result is not None:
                print(f"The factorial of {n} is: {result}")
            else:
                print("Invalid input. Please enter a non-negative integer.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Test cases
test_cases = [0, -5, 1, 'M', '%']

print("Sample Input & Output:")
for test in test_cases:
    print(f"Enter the value of n: {test}")
    main()
    print()
