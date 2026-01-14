#Hangman Game

from word_list import words
import random
import time

hangman_art = { 0:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃       ",
                   " ┃       ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                1:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃       ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                2:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃   │   ",
                   " ┃       ",
                   "━┻━━━━━━━"),
                3:(" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│   ",
                   " ┃       ",
                   "━┻━━━━━━━"),
               4: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃       ",
                   "━┻━━━━━━━"),
               5: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃  ╱    ",
                   "━┻━━━━━━━"),
               6: (" ┏━━━┓   ",
                   " ┃   ╿   ",
                   " ┃   ⬤   ",
                   " ┃  ⟋│⟍  ",
                   " ┃  ╱ ╲  ",
                   "━┻━━━━━━━")
               }

def display_man(wrong_guesses):
    time.sleep(1)
    print("******************")
    time.sleep(0.3)
    for line in hangman_art[wrong_guesses]:
        print(line)
    time.sleep(0.3)
    print("******************")
    time.sleep(1)

def display_hint(hint):
    time.sleep(1)
    print(" ".join(hint))

def display_answer(answer):
    time.sleep(1)
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        time.sleep(1)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            time.sleep(1)
            print("Invalid input")
            continue

        if guess in guessed_letters:
            time.sleep(1)
            print(f"You already typed {guess}, try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("******************")
            print("You Win! Thank you for playing!")
            print("******************")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("******************")
            print("You Lose! Thank you for playing!")
            print("******************")
            is_running = False

if __name__ == "__main__":
    main()