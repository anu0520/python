def fibonacci(n):
    if n <= 0:
        return "Invalid input. N should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


# Input from the user
n = int(input("Enter the value of N: "))

# Get the Fibonacci sequence up to the Nth number
fib_sequence = fibonacci(n)

# Print the Fibonacci sequence
print(" ".join(map(str, fib_sequence)))
