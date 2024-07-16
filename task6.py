def find_maximum_of_three():
    try:
        # Prompting the user to enter three numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        # Finding the maximum of the three numbers
        maximum = max(num1, num2, num3)

        # Printing the result
        print(f"The maximum of the three numbers is: {maximum}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Example usage
find_maximum_of_three()
