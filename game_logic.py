import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(ascii_art.STAGES) - 1

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            print("Wrong!")
            mistakes += 1

        # Check if player has guessed all letters
        all_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                all_guessed = False
                break

        if all_guessed:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("🎉 You saved the snowman!")
            return

    # If loop ends, player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("❄️ The snowman melted... You lost!")