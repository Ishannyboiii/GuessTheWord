import random

words = ["apple", "banana", "orange", "strawberry", "grape", "peach", "pear", "cherry", "raspberry", "blueberry",
         "blackberry", "kiwi", "mango", "pineapple", "watermelon"]

secret_word = random.choice(words)
guess = ""
guess_count = 0

while guess != secret_word and guess_count < 3:
    if guess_count < 3:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        print("You lose")

print("You guessed the word!")
