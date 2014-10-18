
 
# modified (simplified) 21 (poker)
# Strategy of the game: user is dealt at most 2 cards
# whose total should not exceed 21 but should be greater than 
# the computer's dealt hand in order to win.  
 
from random import randint

def concl(i,j, m,n):
    if 22 > i+ j > m+ n:
        print("I won.")
    elif i + j < m + n < 22:
        print("You won.")
    elif  i + j == 22 and m + n < 22:
        print("You won.")
    elif i + j < 22 and m + n == 22:
        print("I won.")
    else:
        print("It's a tie. Game over.")    

n=11
def random1(n):
    return randint(2,n)
def random2(n):
    return randint(2,n)

comp1 = random1(n)  # computer's first card  
comp2 = random2(n)  # computer's second card   
 
q1 = input("Would you like a card? ").lower()  
yes = set(["yes", "ye", "y"])  
if q1 in yes: 
    n=11
    def user_rand1(n): 
        return randint(2,n) 
    user1 = user_rand1(n) 
    print("You have " + str(user1) + " points.")
    q2 = input("Deal another card? ").lower()
    if q2 in yes:
        n=12
        def user_rand2(n):
            return randint(2,n)
        user2 = user_rand2(n)
        print("The second card is worth %s points for a total of %s." % (user2, user1 + user2))
        print("I got %s and %s for a total of %s." % (comp1, comp2, comp1 + comp2))
        concl(comp1, comp2, user1, user2)
    else: 
        print("So you got %s points while I got %s and %s for a total of %s." % (user1, comp1, comp2, comp1 + comp2))
        concl(comp1, comp2, user1, 0) 
else: 
    print("Sorry to see you go. Game Over.")
 
