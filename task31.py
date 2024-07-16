from collections import Counter


def calculate_mean(arr):
    return sum(arr) / len(arr)


def calculate_median(arr):
    sorted_arr = sorted(arr)
    n = len(arr)
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        return (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2


def calculate_mode(arr):
    freq = Counter(arr)
    mode = freq.most_common(1)[0][0]
    return mode


def main():
    # Test cases
    test_cases = [
        [16, 18, 27, 16, 23, 21, 19],
        [26, 28, 37, 26, 33, 31, 29],
        [1.6, 1.8, 2.7, 1.6, 2.3, 2.1, 0.19],
        [0, 160, 180, 270, 160, 230, 210, 190, 0],
        [20, 18, 18, 27, 16, 27, 27, 19, 20],
        [1000, 100, 1000, 100, 1000, 100, 1000, 100, 1000]
    ]

    for arr in test_cases:
        mean = calculate_mean(arr)
        median = calculate_median(arr)
        mode = calculate_mode(arr)

        print(f"Array of elements = {arr}")
        print(f"Mean = {mean}")
        print(f"Median = {median}")
        print(f"Mode = {mode}")
        print()


# Run the main function
main()
