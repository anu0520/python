def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string

# Sample Input
input_string = input("String: ")
reversed_string = reverse_string(input_string)
print(f"Reverse String: {reversed_string}")
