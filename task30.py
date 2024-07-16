def matrix_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_sums = [0] * rows
    col_sums = [0] * cols
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Calculate row sums and column sums
    for i in range(rows):
        for j in range(cols):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]

            # Calculate diagonal sums
            if i == j:
                primary_diagonal_sum += matrix[i][j]
            if i + j == rows - 1:
                secondary_diagonal_sum += matrix[i][j]

    # Print row sums
    for i in range(rows):
        print(f"Sum of {i + 1} row: {row_sums[i]}")

    # Print column sums
    for j in range(cols):
        print(f"Sum of {j + 1} column: {col_sums[j]}")

    # Print diagonal sums
    print(f"Primary diagonal sum: {primary_diagonal_sum}")
    print(f"Secondary diagonal sum: {secondary_diagonal_sum}")


# Test the function with the provided matrix
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_sum(a)
