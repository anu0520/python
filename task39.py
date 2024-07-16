def merge_sorted_lists(list1, list2):
    # Initialize pointers for both lists
    i, j = 0, 0
    merged_list = []

    # Merge the two sorted lists into a third sorted list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Add remaining elements of list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Add remaining elements of list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


def find_kth_largest_number(nums, k):
    if k <= 0 or k > len(nums):
        return None

    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


def find_kth_smallest_number(nums, k):
    if k <= 0 or k > len(nums):
        return None

    sorted_nums = sorted(nums)
    return sorted_nums[k - 1]


def main():
    try:
        # Sample Input lists
        list1 = [1, 2, 4]
        list2 = [0, 3, 6]

        # Merge two sorted lists
        merged_list = merge_sorted_lists(list1, list2)
        print("Merged List:", merged_list)

        # Test Case 1: Find the 2nd largest number
        k = 2
        kth_largest = find_kth_largest_number(merged_list, k)
        print(f"{k}nd Largest number:", kth_largest)

        # Test Case 2: Find the 4th smallest number
        k = 4
        kth_smallest = find_kth_smallest_number(merged_list, k)
        print(f"{k}th Smallest number:", kth_smallest)

        # Test Case 3: Print numbers in reverse order
        print("Numbers in Reverse Order:", merged_list[::-1])

        # Test Case 4: Sum and Average of merged list
        total_sum = sum(merged_list)
        average = total_sum / len(merged_list)
        print(f"Sum of merged list:", total_sum)
        print(f"Average of merged list:", average)

    except ValueError:
        print("Invalid input. Please enter valid integers in the lists.")


# Execute the main function
if __name__ == "__main__":
    main()
