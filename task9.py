def can_vote_in_years(age):
    if age < 0:
        return "Invalid input. Age cannot be negative."
    elif age >= 18:
        return "You are allowed to vote."
    else:
        return f"You are allowed to vote after {18 - age} years."

def main():
    age_input = input("Enter your age: ")

    try:
        # Try to convert the input to a float
        age = float(age_input)

        # Check if the age is a whole number
        if age.is_integer():
            age = int(age)
            print(can_vote_in_years(age))
        else:
            print("Invalid input. Age must be a whole number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Run the main function
main()
