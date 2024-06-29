import random


def show_welcome_message():
    print("Welcome to the Word Guessing Game!")
    print('''
  ____                          _                _____                      
 / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __   |  __ \\ _   _  __ _ _ __ ___  
| |  _ / _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|  | |  \\/ | | |/ _` | '_ ` _ \\ 
| |_| |  __/ | | |  __/ | | (_| | || (_) | |     | | __| |_| | (_| | | | | | |
 \\____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|     |_|\\_\\\\__,_|\\__,_|_| |_| |_|                                      
    ''')
    print("Let's get started...\n")


def get_secret_word():
    word_bank = ['apple', 'alias', 'alloy', 'banana', 'bongo', 'bogey', 'category', 'chains']
    return random.choice(word_bank).upper()


def get_guess(current_display, missed):
    print(f"\nMissed attempts: {missed}\t\tCurrent word: {current_display}")
    guess = input("Enter a letter: ").upper()
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Invalid input. Enter a single alphabetical letter: ").upper()
    return guess


def update_display(secret, current_display, guess):
    return ' '.join([guess if secret[i] == guess else current_display[i * 2] for i in range(len(secret))])


def main():
    show_welcome_message()
    secret_word = get_secret_word()
    display_string = ' '.join('_' * len(secret_word))
    missed_guesses = 0
    total_guesses = 0

    while display_string.replace(' ', '') != secret_word:
        guess = get_guess(display_string, missed_guesses)
        total_guesses += 1

        if guess in secret_word:
            new_display = update_display(secret_word, display_string, guess)
            if new_display == display_string:
                missed_guesses += 1
            display_string = new_display
        else:
            missed_guesses += 1

        if display_string.replace(' ', '') == secret_word:
            print(f"\nCongratulations! You've guessed the word: {secret_word}")
            print(f"Total attempts: {total_guesses}")

    print(f"Game Over! Total guesses: {total_guesses}, Missed guesses: {missed_guesses}")


if __name__ == "__main__":
    main()
