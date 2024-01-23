import random 
import math

#taking input
lower = int(input("Enter lower bound:-"))

#taking input
upper = int(input("Enter the upper bound:-"))

#generating the random numbers between
# the lower and the upper bound
x = random.randint(lower, upper)
print("\n\n You've only",
      round(math.log(upper-lower + 1,2)),
      "chances to guess the integer!\n")

#initializing the number of guesses

count =0

while count < math.log(upper - lower + 1,2):
    count = count + 1

    guess = int (input("Guess a number :-"))

    if x== guess:
        print("Congratulations you guesses it right in ",
              count, "try")
        
        break
    elif x > guess:
        print("You guesses it too low!")
    elif x < guess:
        print("You Guesses it too high!")

#if the guess is more than the number of guesses given
    
if count >= math.log(upper - lower + 1,2):
    print("\n The number is %d" %x)
    print("\t Better luck next time!")

