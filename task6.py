"""Exercise(Balanced Parentheses)
Write a function that checks whether a given string of parentheses is balanced or not using a deque.

Test the function
the output should be in this format
print(is_balanced_parentheses("()")) # True
print(is_balanced_parentheses("({[]})")) # True
print(is_balanced_parentheses("({[]}))")) # False
print(is_balanced_parentheses("({[}])")) # False"""

# Solution
"""from collections import deque

def is_balanced_parentheses(string):
    stack = deque()

    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets[closing_brackets.index(char)] != stack.pop():
                return False
    
    return len(stack) == 0


def main():
    results = []

    while True:
        input_string = input("Enter a string of parentheses: ")
        output = is_balanced_parentheses(input_string)
        results.append((input_string, output))

        choice = input("Would you like to continue? (yes/no): ")
        if choice.lower() == 'no':
            break
        elif choice.lower() != 'yes':
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

    for input_string, output in results:
        print(f'{input_string} # {output}')


if __name__ == '__main__':
    main()"""
############################################################

print("______________________________________________________")

from collections import deque

def is_balanced_parentheses(string):
    stack = deque()
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[char] != stack.pop():
                return False
    
    return len(stack) == 0


def main():
    results = []

    while True:
        input_string = input("Enter a string of parentheses: ")
        output = is_balanced_parentheses(input_string)
        results.append((input_string, output))

        choice = input("Would you like to continue? (yes/no): ")
        if choice.lower() == 'no':
            break
        elif choice.lower() != 'yes':
            print("Invalid choice. Please enter 'yes' or 'no'.")
            continue

    for input_string, output in results:
        print(f'{input_string} # {output}')


if __name__ == '__main__':
    main()
