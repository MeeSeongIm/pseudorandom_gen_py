# guess the number game 
# the computer will pick a number and the user is asked to guess its number in 5 tries. 

from random import randint
n=100 
def randnum(n):
    return randint(1,n)

comp = randnum(n)
 

print("Pick a number between 1 to 100 and your job is to guess my number in 5 tries.")
guess1 = int(input("First guess: "))
if guess1 <= 100 and guess1 >= 1:
    if guess1 == comp:
        print("You won!")
         
    elif guess1 > comp:
        guess2 = int(input("Your guess is higher than mine. Try a smaller number: "))
        if guess2 == comp:
            print("You won!")
        elif guess2 < comp:
            guess3 = int(input("Your guess is smaller than mine. Try something between %s and %s. Guess again: " % (min(guess1, guess2), max(guess1, guess2))))
            if guess3 == comp:
                print("You won!")
            elif guess3 < comp:
                guess4 = int(input("Your guess is smaller than mine. Guess again: " ))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: " ))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                        
            elif guess3 > comp: 
                guess4 = int(input("Your guess is bigger than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                           
            else:
                print("That is not a number between 1 and 100. Re-run the game. ")

        elif guess2 > comp:
            guess3 = int(input("Your guess is bigger than mine. Guess again: "))
            if guess3 == comp:
                print("You won!")
            elif guess3 < comp:
                guess4 = int(input("Your guess is smaller than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                        
            elif guess3 > comp: 
                guess4 = int(input("Your guess is bigger than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                           
            else:
                print("That is not a number between 1 and 100. Re-run the game.") 
        else:
            print("That is not a number between 1 and 100. Re-run the game.")
    elif guess1 < comp:
        guess2 = int(input("Your guess is lower than mine. Try a bigger number: "))

        if guess2 == comp:
            print("You won!")
        elif guess2 < comp:
            guess3 = int(input("Your second guess is smaller than mine. Guess again: "))
            if guess3 == comp:
                print("You won!")
            elif guess3 < comp:
                guess4 = int(input("Your guess is smaller than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                        
            elif guess3 > comp: 
                guess4 = int(input("Your guess is bigger than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                           
            else:
                print("That is not a number between 1 and 100. Re-run the game. ")

        elif guess2 > comp:
            guess3 = int(input("Your second guess is bigger than mine. Try something between %s and %s. Guess again: " % (min(guess1, guess2), max(guess1, guess2))))
            if guess3 == comp:
                print("You won!")
            elif guess3 < comp:
                guess4 = int(input("Your guess is smaller than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                        
            elif guess3 > comp: 
                guess4 = int(input("Your guess is bigger than mine. Guess again: "))
                if guess4 == comp:
                    print("You won!")
                elif guess4 < comp:
                    guess5 = int(input("Your guess is too small. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                elif guess4 > comp:
                    guess5 = int(input("Your guess is too big. Guess again: "))
                    if guess5 == comp:
                        print("You won!")
                    elif guess5 < comp:
                        print("You lose. I picked %s." % (comp))
                    else:
                        print("You lose. I picked %s." % (comp))
                else:
                    print("That is not a number between 1 to 100. Re-run this game.")                           
            else:
                print("That is not a number between 1 and 100. Re-run the game.") 
        else:
            print("That is not a number between 1 and 100. Re-run the game.")   
else:
    print("Sorry. That's not an integer between 1 to 100, including 1 and 100.")
    


