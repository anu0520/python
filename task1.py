def is_valid(s: str) -> bool:
    # Dictionary to hold matching pairs of brackets
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of open brackets
    stack = []

    for char in s:
        if char in bracket_pairs:
            # If the character is a closing bracket, check for its corresponding open bracket
            top_element = stack.pop() if stack else '#'
            if bracket_pairs[char] != top_element:
                return False
        else:
            # If the character is an open bracket, push it onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack

# Testing the function
test_cases = ["()[]{}", "(]", "()", "([)]", "{[]}", ""]

results = {s: is_valid(s) for s in test_cases}

for s, result in results.items():
    print(f'Input: "{s}"\tOutput: {result}')
