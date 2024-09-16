import random

# List of words to guess
words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores
attempts = 8  # Number of allowed attempts


print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ''.join(word_display))
    guess = input("guess a letter ").lower()

    if guess in chosen_word: 
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess

    else:
        print("wrong")
        attempts -= 1 

if '_' not in word_display: 
    print("you won")
    print(word_display)

else: 
    print("you ran out of attempts the word was ", chosen_word)
