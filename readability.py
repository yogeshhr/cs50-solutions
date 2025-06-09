from cs50 import get_string

text = get_string("enter text: ")

# counting letters
letters = 0
for a in text:
    if a.isalpha():
        letters += 1

# counting words
words = len(text.split())

# counting sentences
sentences = text.count(".") + text.count("!") + text.count("?")

# average number of letters per 100 words
L = letters / words * 100

# average number of sentences per 100 words
S = sentences / words * 100

# calculating grade
grade = 0.0588 * L - 0.296 * S - 15.8

# print grade
if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print(f"Grade {round(grade)}")
