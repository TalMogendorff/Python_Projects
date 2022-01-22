mylist = [' ', '0', '']

from random import shuffle

def shuffle_mylist(mylist):
    shuffle(mylist)
    return mylist

shuffled_result = shuffle_mylist(mylist)
print(shuffled_result)

def player_guess():

    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1,2")

    return int(guess)

guess = player_guess()

def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print('Correct !')

    else:
        print('Wrong guess !')
        print(mylist)

check_guess(shuffled_result,guess)