import random
guess = ''
while guess not in('h','t'):
    print('Guess the coin toss!Enter heads or tails:')
    guess = input()
if guess == 'h':
    guess = 1
else:
    guess = 0
toss = random.randint(0,1)  #0 is tails, 1 is heads
#print(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! guess again!')
    guess = input()
    if guess == 'h':
        guess = 1
    else:
        guess = 0
    toss = random.randint(0,1)
    #print(toss)
    
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
