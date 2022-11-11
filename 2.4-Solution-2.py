"""
LESSON: 2.4 - While Loops
EXERCISE: Code Your Own

TITLE: Choose Your Own Adventure Story
DESCRIPTION: A choose-your-own adventure story where some paths can take you back to earlier parts of the story.
"""

# items
hasShovel = False
hasKey = False

print(
    "You are a brave adventurer who has decided to try and escape the Magical Labrynth of Mystery and Whimsy! This will not be an easy task. It has been said that the labrynth sends those who are stuck all the way back to the beginning."
)

while True:

    print(
        "You find yourself in a room that is completely empty except for a red arrow directing you forward."
    )
    path1 = input(
        "There are two different paths in front of you, which one do you follow? (right/left) > "
    )

    if path1 == "right":

        print("You find yourself in a room that contains an assortment of plants.")
        path2 = input(
            "There are two different paths in front of you, which one do you follow? (right/left) > "
        )

        if path2 == "right":

            print(
                "You find yourself in a room that has nothing but a circle of assorted chairs in the center."
            )
            print(
                "The only other thing in this room is an ornate door. You enter through the door... And find yourself at the beginning of the labrynth."
            )

        elif path2 == "left":

            print(
                "You find yourself in a room full on shovels, one in the middle seems to call to you and you decide to pick it up. [You Have Obtained A Shovel]"
            )
            hasShovel = True
            print(
                "The only other thing in this room is an ornate door. You enter through the door... And find yourself at the beginning of the labrynth."
            )

    elif path1 == "left":

        print(
            "You find yourself in an room covered in paintings, sculptures, and other works of art"
        )
        path2 = input(
            "There are two different paths in front of you, which one do you follow? (right/left) > "
        )

        if path2 == "right":

            print(
                "You find yourself in a room where something was very obviously buried."
            )

            if hasShovel:

                print(
                    "Luckily you happen to have a shovel but you don't know how deep it is."
                )
                dig = 0

                while dig < 20:

                    shovels = int(
                        input(
                            "How many times do you want to shovel the ground? (number) > "
                        )
                    )

                    for i in range(shovels):

                        print("*shovel noises*")
                        dig += 1

                    if dig < 20:

                        print(
                            "It looks like you are going to need to do some more shoveling."
                        )

                print("You find a small box in the ground and inside of it is a key.")
                hasKey = True

            else:

                print("You should try and look for a shovel.")

            print(
                "The only other thing in this room is an ornate door. You enter through the door... And find yourself at the beginning of the labrynth."
            )

        elif path2 == "left":

            print(
                "You find yourself in a room with a shiny golden door and an ornate door. Clearly the golden one is more special, but it has a lock on it."
            )

            if hasKey:

                print(
                    "Luckily you have the exact key to unlock that door. You step through the door."
                )
                break

            else:

                print(
                    "You should try and look for a key, but for now the only option is to head through the ornate door. Stepping through... you find yourself at the beginning of the labrynth."
                )

print("You have escaped the Magical Labarynth of Mystery and Whimsy!")
