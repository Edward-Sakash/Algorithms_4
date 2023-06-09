"""Exercise(Reverse a Sentence):
Write a function that takes a sentence as input and uses a deque to reverse the words in the sentence.

Test the function
print(reverse_sentence("Hello, world!")) # world! Hello,
print(reverse_sentence("Python is fun")) # fun is Python
print(reverse_sentence("I love coding")) # coding love I"""

# Solution 
from collections import deque

def reverse_sentence(sentence):
    words = sentence.split()
    word_deque = deque(words)
    reversed_words = []
    
    while word_deque:
        reversed_words.append(word_deque.pop())
    
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


# Test the function
input1 = input("Enter the first sentence: ")
input2 = input("Enter the second sentence: ")
input3 = input("Enter the third sentence: ")

print(reverse_sentence(input1))
print(reverse_sentence(input2))
print(reverse_sentence(input3))
