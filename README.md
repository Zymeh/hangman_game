# hangman_game

# Table of Contents
1. [Introduction](#introduction)
1. [Game Versions](#versions)
    - [Version 1](#V1)
    - [Version 2](#V2)
    - [Version 3](#V3)
    - [Version 4](#V4)
    - [Version 5](#V5)


## Introduction
This project, assigned by AiCore, provided an excellent opportunity for me to apply and reinforce the knowledge I've gained throughout the course. The primary objective of this project was to leverage the concept of classes, which proved to be an invaluable tool. Classes enable the creation of instances that can be used with class methods to execute tasks tailored to each instance. 

## Versions

There were 4 milestones in this project, which correlate with each of the versions below.

### V1
Here we chose a random word from a given list of words using `random.choice()`. We then asked for a users input. With this input, we then employ validity checks via an `if-else` statement. This is necessary since we require a singular alphabetical character in order to play Hangman.

### V2
We created the `check_guess` function, where the user input is an argument. This formats the users input and then simply checks if said input is in the word to be guessed. A message is then supplied, letting the player know if their guess is correct or not.

We employed a function `ask_for_input` that asks for an input and uses the previous codes validity checks in an indefinite `while` loop. This only stops when a correct input is given. This input is then passed into `check_guess()`. 

### V3
I finally introduce the Hangman class. We initialise the arguments passed into the class (with them being `word_list` and `num_lives` (default= 5)) and the attributes that belong to that instance of the class. The attributes are: the random word chose, list of guesses the user has inputted, the number of letters in the word and the structure of the word to be guessed (with each character represented as an `_` in a list).

I employed the function `check_guess()` from V2 as a method, with some adaptations. We added: If the user input is in the word to be guessed, the user input replaces the `_` from the word structure list in the corresponding position(s). And, the number of letters left to guess is decreased accordingly. If the user input is incorrect, the number of player lives is decreased by 1.

I then employed the function `ask_for_input()` from V2 as a method, again adding to its functionality. This time, we added checks to see if the character had already been guessed, if it had not been guessed and the input is valid, we call the `check_guess` method and append the guess to the list of guesses.

I also added docstrings throughout. 

### V4 
Here, I created a function which actually allows us to play the game. The arguments the function (`play_game`) takes in is the users list of words they want to guess. We then initialise a game state with this list. Then, in an indefinite `while` loop, we firstly print the structure of the word to be guessed. Then we perform checks in an `if-elif-else` statement. If the player lives reaches 0, the game stops as we return a message telling the player this news. If this condition is not met, we check if the number of letters to be guessed is greater than 0. If it is, another round is played by using the `ask_for_input` method. However, if this condition is not met (i.e. the number of letters remaining to be guessed is 0), the function ends as we return a message telling the player they have won.

I also improved the existing docstrings, and added one for the new function `play_game`.

### V5 
TBA
