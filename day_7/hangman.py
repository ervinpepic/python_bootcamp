from cmath import log
import random
from stages_logo import stages, logo
from word_list import word_list

print(logo)

chosen_word = random.choice(word_list)
lives = 6
display = []

for _ in range(len(chosen_word)):
    display.append("_") 

while "_" in display and lives > 0:
    guess = input("Gues a letter: ").lower()
    if guess in display:
        print(f"You already tried the {guess} letter")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f"Unfortunately, the letter {guess} is not in the word, you have {lives} left.")
        lives -= 1
        print(stages[lives])
        
        if lives == 0:
            print("YOU LOSE ALL OF YOUR LIVES!")

    print(f"{' '.join(display)}")


