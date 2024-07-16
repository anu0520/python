def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Set the number of lines for the pattern
n = 5
print_pattern(n)
