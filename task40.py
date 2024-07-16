def find_mth_maximum(arr, m):
    if m <= 0 or m > len(arr):
        return None

    sorted_arr = sorted(set(arr), reverse=True)  # Sorting unique elements in descending order
    return sorted_arr[m - 1]


def find_nth_minimum(arr, n):
    if n <= 0 or n > len(arr):
        return None

    sorted_arr = sorted(set(arr))  # Sorting unique elements in ascending order
    return sorted_arr[n - 1]


def main():
    try:
        # Sample Input
        arr = [14, 16, 87, 36, 25, 89, 34]
        M = 1
        N = 3

        # Find Mth maximum and Nth minimum
        mth_max = find_mth_maximum(arr, M)
        nth_min = find_nth_minimum(arr, N)

        if mth_max is not None and nth_min is not None:
            # Calculate sum and difference
            total_sum = mth_max + nth_min
            difference = abs(mth_max - nth_min)

            # Output the results
            print(f"{M}st Maximum Number = {mth_max} {N}rd Minimum Number = {nth_min}")
            print(f"Sum = {total_sum}")
            print(f"Difference = {difference}")
        else:
            print("Invalid input. Please check the values of M and N.")

    except ValueError:
        print("Invalid input. Please enter valid integers in the array.")


# Execute the main function
if __name__ == "__main__":
    main()
