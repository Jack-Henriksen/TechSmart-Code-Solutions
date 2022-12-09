"""
LESSON: 1.3 - Expressions
EXERCISE: Code Your Own

TITLE: Multiplication Table Line Locator
DESCRIPTION: Given a user's input, prints the lines that value appears on; from lines 1 to 12.
"""

number = int(input("Give me a number > "))
finalString = "On a multiplication table, " + str(number) + " appears on lines: "

if number % 1 == 0:
    finalString += str(1) + " "

if number % 2 == 0:
    finalString += str(2) + " "

if number % 3 == 0:
    finalString += str(3) + " "

if number % 4 == 0:
    finalString += str(4) + " "

if number % 5 == 0:
    finalString += str(5) + " "

if number % 6 == 0:
    finalString += str(6) + " "

if number % 7 == 0:
    finalString += str(7) + " "

if number % 8 == 0:
    finalString += str(8) + " "

if number % 9 == 0:
    finalString += str(9) + " "

if number % 10 == 0:
    finalString += str(10) + " "

if number % 11 == 0:
    finalString += str(11) + " "

if number % 12 == 0:
    finalString += str(12) + " "

print(finalString)
