from tkinter import *

import random
import string
class Hangman:
    '''This class is used to play the Hangman Game.

    Attributes:
        word_list (`list`): list of words which need to be guessed for the hangman game.
        num_lives (`int`): number of lives the player has.
        word (`str`): this generates a random word from the list of words supplied.
        list_of_guesses (`list`): a list which displays the users previous letter guesses.
        num_letters (`str`): this is a count of how many letters there are left to guess.
        word_guessed (`list`): this lets the user know the structure of the word with underscores, when they guess something correct, the underscore are replaced with thier guess.

    '''
    def __init__(self, word_list, num_lives):
        '''Initialises the instance based on a list of words given and the number of lives the player defines.

        Args:
            word_list (`list` of `str`): initialises the list of words given to be guessed.
            num_lives (`int`): initialises the number of lives for the given instance, the default number of lives is 5
        '''
        self.word_list = word_list
        self.num_lives = num_lives

        word = random.choice(self.word_list)
        word = word.translate(str.maketrans('', '', string.punctuation))

        self.word = word.lower()
        self.list_of_guesses = []
        self.num_letters = len(self.word)

        self.word_guessed = []
        for _ in range(self.num_letters):
            self.word_guessed.append('_')

    def check_guess(self, player_guess):
        '''This function checks if the guessed character is in the word.

        First, the user input is put into lower case. Then, if the guess is in the word, the index of the character is found and used to replace the '_' in word_guessed at the correct location, and finally the total number of characters in the word is reduced accordingly. If the guess incorrect, the number of lives decreases by 1.

        Args:
            player_guess (`str`): the players choice of character to be tested.

        '''
        player_guess = player_guess.lower()
        if player_guess in self.word:
            for index_of_word in range(len(self.word)):
                if player_guess == (self.word)[index_of_word]:
                    self.word_guessed[index_of_word] = player_guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1



    def ask_for_input(self,player_guess):
        '''This function asks for and checks the user input.

            Here we ensure the user input is one unique alphabetic character. If it is valid, the charecter is placed in list_of_guesses.
        '''
        if len(player_guess) != 1 or player_guess.isalpha() == False:
            None
        elif player_guess in self.list_of_guesses:
            None
        else:
            self.check_guess(player_guess)
            (self.list_of_guesses).append(player_guess)
            return


def play_game(word_list, number_of_lives= 5):
    '''This function allows us to play hangman.

    We initialise an object in the Hangman class with the users input. We then imploy a window to play the game. The user simply types in their guess. It is validated, an error message is displayed in the window if its not valid. it then checkes if the input is in the word the word the user is guessing. and depending on this, the display window is updated accordingly ( lives decreased if its wrong, or the template word is updated if its right). When the game ends, the `enter` button on the display is removed. 

    Args: 
        word list (`list` of `str`): List of words the user wants to play with. 
        number_of_lives (`int` (optional)): Number of lives the user wishes to play with. 

    Return: 
        Lets the player know if they have won (lenght of the word to be guessed is 0) or lost (ran out of lives).

    '''
    game = Hangman(word_list, number_of_lives)
    root = Tk()
    root.title("Hangman Game")

    def button_command():
        # gets users input from the entry field
        player_guess = user_input.get()
        user_input.delete(0, END)
        if player_guess in game.word_guessed:
            result_label.config(text="You already tried that letter!")
            return 
        if len(player_guess) != 1 or player_guess.isalpha() == False:
            result_label.config(text='Invalid input. Please enter a single alphabetical character')
            return
        # call the check_guess method with the input
        game.ask_for_input(player_guess)
        
        # update the labels to reflect the game state
        word_to_be_guessed_2.config(text=game.word_guessed)
        num_of_lives_2.config(text=game.num_lives)
        letters_guessed_2.config(text=game.list_of_guesses)
        

        # check if the game is won or lost
        if game.num_lives == 0:
            result_label.config(text="You lost!")
            button.destroy()
        elif game.num_letters == 0:
            result_label.config(text="GG! you have won the game")
            button.destroy()
            return

    # word to be guessed
    word_to_be_guessed_1 = Label(root, text= "Word to be guessed:")
    word_to_be_guessed_2 = Label(root, text= game.word_guessed)

    word_to_be_guessed_1.grid(row= 0, column= 0)
    word_to_be_guessed_2.grid(row= 0, column= 1)

    # lives
    num_of_lives_1 = Label(root, text= 'Remaining lives:')
    num_of_lives_2 = Label(root, text= game.num_lives)

    num_of_lives_1.grid(row= 1, column= 0)
    num_of_lives_2.grid(row= 1, column= 1)

    # letters guessed
    letters_guessed_1 = Label(root, text= 'Letters guessed:')
    letters_guessed_2 = Label(root, text= game.list_of_guesses)

    letters_guessed_1.grid(row=2, column= 0)
    letters_guessed_2.grid(row=2, column= 1)

    user_input = Entry(root, width= 50)
    button = Button(root, text="Enter", command=button_command)
    button.grid(row=3, column=0)
    user_input.grid(row= 3,column= 1)

    result_label = Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2)


    root.mainloop()

play_game(['in', 'mathematics', 'specifically', 'commutative', 'algebra', 'hilberts', 'basis', 'theorem', 'says', 'that', 'a', 'polynomial', 'ring', 'over', 'a', 'noetherian', 'ring', 'is', 'noetherian'])