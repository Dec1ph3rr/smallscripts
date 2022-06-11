import random as r

randomnum = r.randint(0,10)

print("Guess the number I'm thinking of between 0 and 10: ")
guess = input()

if guess == randomnum: 
    print("That's exactly right! I was thinking of ", randomnum)
else: 
    print("That's wrong. I was thinking of", randomnum)