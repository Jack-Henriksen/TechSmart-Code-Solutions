"""
LESSON: 2.3 - Booleans
EXERCISE: Code Your Own

TITLE: Afternoon Planner
DESCRIPTION: Tells the user how they should spend their afternoon based on their mood and available time.
"""

time = int(input("How much free time do you have this afternoon? (in minutes) > "))
mood = input(
    "Are you feeling more relaxed or energetic this afternoon? (relaxed/energetic) > "
)
print("My brilliant suggestion for how you should spend your afternoon: ")

if time >= 120:

    if mood == "relaxed":

        print("You should watch a movie")

    elif mood == "energetic":

        print("You should go for a long bike ride")

elif time <= 20:

    print("You don't have very much time to do anything")

else:

    if mood == "relaxed":

        print("You should bake some cookies")

    elif mood == "energetic":

        print("You should go walk")
