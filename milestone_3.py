import random
# below we simply define a list, and then select a random word from it. 
word_list = ['mango', 'apple', 'apricot', 'cherry', 'blueberry']
word = random.choice(word_list)

def check_guess(guess): # this simply checks if the guess is in the word.
    guess = guess.lower()
    if guess in word: 
        print(f'Good guess! {guess} is in word')
    else:
        print(f'sorry, {guess} is not in the word.')

def ask_for_input(): # this checks if the input is valid, continuosly asks for input if it isnt valid. but if it is valid, it uses the check_guess function to check if the guess is in the word.
    while True: 
        guess = input('Please enter one alphabetical charecter: ')
        if guess.isalpha() == True & len(guess) == 1:
            break
        else:
            print('Invalid letter, please enter a single alphabetical charecter')
    check_guess(guess)
    return 
