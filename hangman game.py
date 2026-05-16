import random

# List of words
word_list = ["apple", "tiger", "chair", "water", "pizza"]

# Randomly choose a word
secret_word = random.choice(word_list)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses allowed
wrong_guesses = 6

# Hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Main game loop
while wrong_guesses > 0:

    # Show current hangman stage
    print(hangman_stages[6 - wrong_guesses])

    # Display hidden word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly.")
        break

    # Ask player for input
    player_guess = input("Enter a single letter: ").lower()

    # Error if more than one letter entered
    if len(player_guess) != 1:
        print("Error: Please enter only ONE letter.")
        continue

    # Check if already guessed
    if player_guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Save guessed letter
    guessed_letters.append(player_guess)

    # Check guess
    if player_guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses -= 1
        print("Wrong guess!")
        print("Remaining guesses:", wrong_guesses)

# If player loses
if wrong_guesses == 0:
    print(hangman_stages[6])
    print("\nGame Over!")
    print("The correct word was:", secret_word)