"""Exercise(Palindrome Checker):
Write a function that checks whether a given string is a palindrome or not using a deque.
Hint:
use the popleft() und pop() methods"""

# Solution
# for one value
"""from collections import deque

def is_palindrome(string):
    char_deque = deque(string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    string = input("Enter a string: ")
    
    if is_palindrome(string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == '__main__':
    main()
"""

#########################################
print("_____________________________________")

# Solution
# for three values
"""from collections import deque

def is_palindrome(string):
    char_deque = deque(string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    string1 = input("Enter the first palindrome: ")
    string2 = input("Enter the second palindrome: ")
    string3 = input("Enter the third palindrome: ")
    
    print(is_palindrome(string1))
    print(is_palindrome(string2))
    print(is_palindrome(string3))


if __name__ == '__main__':
    main()"""

#################################################

from collections import deque

def is_palindrome(string):
    char_deque = deque(string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")
    
    print(f'is palindrome "{string1}" # {is_palindrome(string1)}')
    print(f'is palindrome "{string2}" # {is_palindrome(string2)}')
    print(f'is palindrome "{string3}" # {is_palindrome(string3)}')


#if __name__ == '__main__':
main()
