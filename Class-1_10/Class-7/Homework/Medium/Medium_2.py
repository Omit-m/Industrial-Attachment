"""
[*] Count Vowels in a String:
    Write a program that counts the number of vowels in a string provided by the user using a for loop.
"""

n = input(" Enter a word : ")
vowels = 'aeiouAEIOU'
vowel_count = 0

for char in n:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")