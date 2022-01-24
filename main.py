import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
display = []

for char in chosen_word:
    display.append("_")

end_game = False
player_lives = 6

while not end_game:

    guess = input("Guess a letter:\n").lower()

    if guess in display:
        print(f"You already chose {guess}. Try a new letter.")

    if len(guess) > 1:
        print("Please enter a single letter.")
        guess = input("Guess a letter:\n")
    else:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess

        print(display)

    if guess not in chosen_word:
        player_lives -= 1
        print(f"You guessed {guess}. That's not in the word. Try again")
        if player_lives == 0:
            end_game = True
            print("You've died.")

    if "_" not in display:
        end_game = True
        print("You've escaped the gallows! Congratulations!!")

    print(hangman_art.stages[player_lives])
