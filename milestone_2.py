import random

word_list = ['mango', 'apple', 'apricot', 'cherry', 'blueberry']

word = random.choice(word_list)

guess = input('Please enter a single letter: ')

if len(guess) == 1 and guess in "qwertyuioplkjhgfdsazxcvbnm":
    print('Good guess!')
else:
    print('Oops! That is an invalid input')
