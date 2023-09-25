import random

class Hangman: # here, we are initialising the values for the instance.
    def __init__(self, word_list, num_lives= 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.list_of_guesses = []
        self.num_letters = len(self.word)

        self.word_guessed = []
        for _ in range(self.num_letters):
            self.word_guessed.append('_')

    def check_guess(self, player_guess): # here we check if the players selection is a character of the word they are tying to guess 
        player_guess = player_guess.lower()
        if player_guess in self.word:
            print(f'Good guess! {player_guess} is in the word.')
            index_of_guess = (self.word).find(player_guess)
            self.word_guessed[index_of_guess] = player_guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {player_guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
        return


    def ask_for_input(self): # we get the players input, check it is actually a one alphabetical character, check if its already been used and finally add it to the list of guesses ( if its nto already a guess)
        while True:
            player_guess = input('Please enter one alphabetic character:')
            if len(player_guess) != 1 or player_guess.isalpha() == False:
                print('Invalid letter. PLease enter a single alphabetical character')
            elif player_guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                self.check_guess(player_guess)
                (self.list_of_guesses).append(player_guess)