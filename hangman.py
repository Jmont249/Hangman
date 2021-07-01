"""Function to fetch words."""

import random
import re
WORDLIST = 'words.txt'
LIVES = 6
player_name = input("Enter your Name: ")
print('Player:', player_name)


def get_random_word(min_word_length):
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for line in f:
            for word in line.split(' '):
                if '(' in word or ')' in word:
                    continue
                word = word.strip().lower()
                if len(word) < min_word_length:
                    continue
                num_words_processed += 1
                if random.randint(1, num_words_processed) == 1:
                    curr_word = word
    return curr_word



def print_correct(end='\n'):
    global correct
    print(' '.join(correct), end=end)

'''wrong attempt
def game():
    global correct
    global LIVES
    word = get_random_word(5)
    print(word)
    length = len(word)
    correct_ans = 0
    correct = ['_' for i in range(length)]
    incorrect = []


    print('live =',LIVES)
    while LIVES > 0:
        print_correct()
        print('letter Guessed: ',incorrect)
        print('Lives =',LIVES)
        if correct_ans==length:
            print(player_name, "Won")
            break
        letter = input("Guess Character: ").lower()
        if len(letter) != 1:
            print("You must Enter a single letter")
            continue

        if letter in word:
            index = word.index(letter)
            for i in range(index+1,length):
                print(i)
                index_2 = word.find(letter,i)
                if index_2!=-1:
                    print(index_2)
                    correct[index_2] = letter
                    correct_ans+=1
                    continue
                else:
                    correct[index] = letter
                    correct_ans+=1
                    break
        else:
            incorrect.append(letter)
            LIVES -= 1

    else:
        print(player_name, "Lose.")
    ans = input(" Want to Play Again\t(y/n): ").lower()
    if ans =='y':
        LIVES = 6
        game()

'''
def game2():
    global correct
    global LIVES
    word = get_random_word(5)
    length = len(word)
    correct_ans = 0
    correct = ['_' for i in range(length)]
    incorrect = []


    print('live =',LIVES)
    while LIVES > 0:
        print_correct()
        print('letter Guessed: ',incorrect)
        print('Lives =',LIVES)
        if correct_ans==length:
            print(player_name, "Won")
            break
        letter = input("Guess Character: ").lower()
        if len(letter) != 1:
            print("You must Enter a single letter")
            continue
        change =0
        if  letter in correct:
            continue
        for j,i in enumerate(word):

            if letter==i:
                correct[j] = i
                change =1
                correct_ans+=1

        if not change:
            incorrect.append(letter)
            LIVES -= 1

    else:
        print(player_name, "Lose.")
    ans = input(" Want to Play Again\t(y/n): ").lower()
    if ans =='y':
        LIVES = 6
        game2()

if __name__ == '__main__':
    game2()