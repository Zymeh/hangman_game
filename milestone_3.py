import random
# below we simply define a list, and then select a random word from it. 
word_list = ['mango', 'apple', 'apricot', 'cherry', 'blueberry']
word = random.choice(word_list)

def check_guess(player_guess): # this simply checks if the guess is in the word.
    player_guess = player_guess.lower()
    if player_guess in word: 
        print(f'Good guess! {player_guess} is in word')
    else:
        print(f'sorry, {player_guess} is not in the word.')

def ask_for_input(): # this checks if the input is valid, continuosly asks for input if it isnt valid. but if it is valid, it uses the check_guess function to check if the guess is in the word.
    while True: 
        player_guess = input('Please enter one alphabetical charecter: ')
        if player_guess.isalpha() == True & len(player_guess) == 1:
            break
        else:
            print('Invalid letter, please enter a single alphabetical charecter')
    check_guess(player_guess)
    return 
