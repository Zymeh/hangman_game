import random

class Hangman: # here, we are initialising the values for the instance.
    '''This class is used to play the Hangman Game.

    Attributes:
        word_list (list): list of words which need to be guessed for the hangman game.
        num_lives (int): number of lives the player has.
        word (str): this generates a random word from the list of words supplied.
        list_of_guesses (list): a list which displays the users previous letter guesses.
        num_letters (str): this is a count of how many letters there are left to guess.
        word_guessed (list): this lets the user know the structure of the word with underscores, when they guess something correct, the underscore are replaced with thier guess.

    '''
    def __init__(self, word_list, num_lives= 5):
        '''Initialises the instance based on a list of words given and (optional) the number of lives the player defines.

        Args:
            word_list (:obj:`list` of :obj:`str`): initialises the list of words given to be guessed.
            num_lives (:obj:`int`, optional): initialises the number of lives for the given instance, the default number of lives is 5
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.list_of_guesses = []
        self.num_letters = len(self.word)

        self.word_guessed = []
        for _ in range(self.num_letters):
            self.word_guessed.append('_')

    def check_guess(self, player_guess):
        '''This function checks if the guessed character is in the word.

        First, the user input is put into lower case. Then, if the guess is in the word: a message is printed indicating this, the index of the character is found which is then used to replace the '_' in word_guessed at the correct location, and finally the total number of characters in the word is reduced accordingly. If the guess incorrect, the number of lives decreases by 1, then 2 messages tell the player their guess is wrong and their remaining lives they have left.

        Args:
            player_guess (str): the players choice of character to be tested.

        Returns:
            TBA
        '''
        player_guess = player_guess.lower()
        if player_guess in self.word:
            print(f'Good guess! {player_guess} is in the word.')
            for i in range(len(self.word)):
                if player_guess == self.word[i]:
                    self.word_guessed[i] = player_guess
                    self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print(f'Sorry, {player_guess} is not in the word')
            print(f'You have {self.num_lives} lives left')
        return


    def ask_for_input(self): # we get the players input, check it is actually a one alphabetical character, check if its already been used and finally add it to the list of guesses ( if its nto already a guess)
        '''This function asks for and checks the user input.

            An indefinite while loop is employed to ensure the user input is one unique alphabetic character. If it is valid, the charecter is placed inside the list_of_guesses.
        '''
        while True:
            player_guess = input('Please enter one alphabetic character:')
            if len(player_guess) != 1 or player_guess.isalpha() == False:
                print('Invalid letter. PLease enter a single alphabetical character')
            elif player_guess in self.list_of_guesses:
                print(f'You already tried that letter!')
            else:
                self.check_guess(player_guess)
                (self.list_of_guesses).append(player_guess)