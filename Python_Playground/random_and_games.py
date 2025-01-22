import random
"""
The first thing is to import the random module.
It has a method called randomit() that we used to generate a random
number in a range of 1 to 10.
"""
generatedNumber = random.randrange(1, 10)
"""
Then we accept the input from the user and ask 
the user to guess the number
"""

userGuess = int(input("Enter a number between 1 - 10: "))
"""
If the guess of the user matches the randomly generated number,
then we print the result accordingly.
"""

if userGuess == generatedNumber:
    print("You have got it right!")
elif userGuess < generatedNumber:
    print("Your number is too low!")
else:
    print("Your number is too high!")
