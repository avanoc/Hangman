import csv
import random

def main():
    
    TRIES = 5

    # Print rules
    print(f"You have {TRIES} tries to guess the correct word.")
    print("If you guess a letter in the correct place, it will appear in uppercase.")
    print("If you guess a letter in an incorrect place, it will appear in lowercase.")
    print("Keep in mind that any letter that you guess, may be repeated in the word.")

    # Select number of letters in word:
    try:
        num_letters = select_letters()
    except IndexError:
        print("Please enter a valid number.")

    # Randomly choose a word with that many letters:
    with open("words.csv") as dic:
        reader = csv.reader(dic)
        chosen_row = random.choice(list(reader))
        word = chosen_row[num_letters - 3]

    # Set initial try
    i = 0
    
    # Call the functions for the user to guess the word and check if it's correct
    while i < 5:
        guess = guess_word(num_letters)
        if check_word(guess, word.upper()):
            
            # Congratulate player when wining:
            print(f"{guess} is correct!")
            print("Congratulations! You've won!")
            break
        else:
            
            # Add one try for each word guessed wrong
            i += 1
    
    # Return final message when 5 tries have been reached
    if i == TRIES:
        print("Sorry, you've lost")
        print(f"The correct word is {word}")
        

def select_letters():

    # Prompt user to select how many letters should the word have:
    while True:
        letters = input("Select number of letters (3 to 7): ")

        # Only accept numbers:
        if letters.isnumeric():
            break
    return int(letters)


def guess_word(l):
    
    # Prompt user to guess for the word, and turn it to uppercase:
    while True:
        guessed = input(f"Enter a {l} letter word: ").upper()
        
        # Only accept alphabetic characters:
        if guessed.isalpha():
            break
    return guessed


def check_word(guessed, original):
    clues = []
    length = len(original)

    # If the guessed word is not as long as the original word, return False:
    if length != len(guessed):
        print(f"You haven't entered a {length} letter word.")
        return False
    
    # If the guessed word matches the original, return True:
    elif guessed == original:
        return True
    
    # If not, check if some words are correct, and print out correct words, but return False:
    else:        
        for i in range(length):

            # Check if the letter is in the same position:
            if guessed[i] == original[i]:
                clues.append(guessed[i])

            # Check if some letter is equal, though in another position:
            elif guessed[i] in original and guessed[i] not in clues:
                clues.append(guessed[i].lower())
            
            # If letter is not in the word:
            else:
                clues.append("_")

        print(*clues)
        return False   


if __name__ == "__main__":
    main()