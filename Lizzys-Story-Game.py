#== comparison
#< less than
#<= less than equal to
#> greater than
#>= greater than equal to

# or One needs to be true
# and Both need be true to be true
# not oppisite of True or False

"""Build a story game with different scenarios using if statements.
Make sure you use the health variable to keep track of health and have the users health change
in different scenarios"""

from time import sleep
import sys

def typewriter(str):
    for x in str:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.04)
    print('')

#Set health by doing health = health + or - <number here>
typewriter("You are on a mission to obtain an Animal Crossing Switch...")
typewriter("You find out there is ONE in stock at your local Best Buy...")
typewriter("You drive to Best Buy and make it inside...")
typewriter("You look left and look right...THEY are everywhere...")
typewriter("Scalpers...")
typewriter("You need to make it to the AC switch before they do...")

choice = input("Do you want to go left or right? (L/R) ")

if choice == "L":
    #Examples
    typewriter("You turn left and a BB employee jumps right in front of your path...")
    typewriter("He asks 'Do you need any help finding anything????' ")
    typewriter("You say 'No thank you' as you walk away.")
    typewriter("He grabs your arm...holding you in place...")
    typewriter("You think to youself...I need to break free or I will lose my chance at a AC Switch...")
    typewriter("You look around...")

    choice = input("Grab something? (1/2) ")
    if choice == "1":
        typewriter("You grab his retractable nametag...")
        typewriter("You start to wrap it around his arm very tight so he could lose curculation...")
        typewriter("He lets go...you make a run for it.")
        typewriter("You make it to the AC Switch and claim it as yours!")
        typewriter("VICTORY!")

    elif choice == "2":
        typewriter("You grab a on display iPhone 11 Pro Max...you ask him to tell you more about this phone...")
        typewriter("He lets go and starts to ramble about the specs of the phone...")
        typewriter("You make a run for it...")
        typewriter("You look back...and see a iPhone 11 Pro Max being thrown your way...")
        typewriter("You try and dodge...but are too slow...it hits you in the head...you knock out.")
        typewriter("You lose your chance at an AC Switch...")
        typewriter("YOU LOSE!")

elif choice == "R":
    
    typewriter("You turn right and you see HIM...")
    typewriter("George...the local infamous Scalper...")
    typewriter("You start to pace faster to pass him up...")
    
    choice = input("You get closer to him...do you 1.Confront him or 2.Keep going? (1/2) ")

    if choice == "1":
        typewriter("You confront him and tell him you know who he is and what he does is not right...")
        typewriter("He chuckles...and just tells you 'Its a business...' ")
        typewriter("You both start pacing faster to the back of the store...")
        
        choice == input("You think of a way to stop him... you...? (1/2) ")

        if choice == "1":
            typewriter("...PUNCH him in the face and make him stop in his tracks")
            typewriter("His nose is bleeding and BB employees gather aroung him.")
            typewriter("You try to make a run for it but two other BB employees grab you and escort you outside the store.")
            typewriter("Mission failed...")
            typewriter("YOU LOSE!")
        
    elif choice == "2":
        
        typewriter("You keep going and start to think of Sonic the Hedgehog and start to run so fast...")
        typewriter("You were able to grab the AC Switch and make 3 laps around the store before George even makes his next step.")
        typewriter("You go to check out...")
        typewriter("SUCCESS!")
        typewriter("YOU WIN!")
        
