"""
LESSON: 2.5 - Randomness & Libraries
EXERCISE: Code Your Own

TITLE: Adventure Story: A Story of Adventure
DESCRIPTION: An adventure story where treasure is in a randomized spot.
"""

import random

# Locations 3 & 4 are treated as on location initially, but then it randomizes 50/50 between the two.
"""
1: Fruit Room
2: Plant Room
3: Sun Door
4: Moon Door
"""

treasureLocation = random.randint(1, 3)
if treasureLocation == 3:
    treasureLocation = random.randint(3, 4)

rightBridgeBroken = False
beenToGem = False

print("Talk of a precious treasure has led you to a mysterious and dangerous temple.")
print(
    "There will be multiple paths in this temple that may lead to the treasure, but may also lead to dangerous traps."
)

while True:

    print(
        "As you enter the temple, you come across a large hole that blocks your path, luckily there are two bridges across the hole"
    )
    if rightBridgeBroken:
        print("For some strange reason the right bridge seems to be repaired")
    bridgeChoice = input(
        "Do you wish to go across the right bridge or the left bridge? (right/left) > "
    )

    if bridgeChoice == "right":

        rightBridgeBroken = True
        print(
            "As you are walking across the right bridge, it breaks and you fall into the hole..."
        )
        print("Luckily the hole isn't very deep and you find yourself in another room.")
        print(
            "In this room you find two doors, one is marked with a gem and the other is marked with an apple."
        )
        doorChoice = input("Which door do you go through? (gem/apple) > ")

        if doorChoice == "apple":

            print("In this room you find yourself surrounded by various fruits")

            if treasureLocation == 1:

                print("On top of all the fruits you see... A golden relic!")
                break

            else:

                print("There is a single door at the end of the room.")
                print(
                    "Going through the door you find yourself... In front of the temple entrance?"
                )

        if doorChoice == "gem":

            print("In this room there is pile of assorted rocks.")
            print(
                "Beyond the pile of rocks, there are two pedistals with what looks like to be..."
            )
            print("2 Different golden relics! But, one must be a fake.")
            if beenToGem:
                print(
                    "That's strange, the " + pedistalChoice + " relic is still there."
                )
            pedistalChoice = input("Which one do you choose? (left/right) > ")
            print(
                "As you pick up the "
                + pedistalChoice
                + " relic it dissolves in your hands and everything goes dark"
            )
            if beenToGem:
                print("It looks like both relics were fake and you were fooled.")
            print(
                "After a few seconds you find yourself... In front of the temple entrance?"
            )

            beenToGem = True

    if bridgeChoice == "left":

        print(
            "You successfully cross the bridge and on the other side there are two doors."
        )
        print("The right door has a golden frame, the left door has a marble frame.")
        doorChoice = input("Which door do you go through? (left/right) > ")

        if doorChoice == "right":

            print(
                "As you enter, you notice that the room is covered in vines and other plants."
            )

            if treasureLocation == 2:

                print("In a bed of flowers you spot... A golden relic!")
                break

            else:

                print("The plants start to grab onto you. You are pulled to a wall")
                print(
                    "As you are pulled into the vines you find that you... Are suddenly back at the temple entrance?"
                )

        if doorChoice == "left":

            print("In the room you see two different doors.")
            print("One door has a sun on it, the other has a moon.")
            doorChoice = input("Which door do you want to go through? (sun/moon) > ")

            if (doorChoice == "sun" and treasureLocation == 3) or (
                doorChoice == "moon" and treasureLocation == 4
            ):

                print("Inside the room there is a nothing but a small pedistal")
                print("On top of that pedistal there is... A golden relic!")
                break

            else:

                print(
                    "As you enter the room... You find yourself at the temple entrance?"
                )

print(
    "As you pick up the golden relic you are magically transported out of the temple."
)
print("You have successfully plundered the treasure and escaped the temple!")
