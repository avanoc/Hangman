# Hangman
#### Description:
This is the python version of the game where you have to guess a given word.

#### How to play:
First select the number (between 3 and 7) of letters you want to play with. If you don't enter a numeric character, or
you enter any number that's not between 3 and 7, you'll be repromted.
The program will access a csv file with 500 words (in english) for each amount of letters, and randomly select a word.
Then, you have to guess. You have 5 tries to guess the correct word.
You may enter any letter combination in upper or lowercase, but if you enter a non alphabetic character you will loose 
one try and you'll be reprompted for a word.
For each incorrect guess, you'll loose a try.
If you enter a word with a letter that is in the word-to-guess, and that letter is in the correct position, it will appear
in uppercase. If it's not in the correct position, it will appear in lowercase. If the letter is not in the word-to-guess
you'll se a "_".

I hope you like it! Have fun :D
