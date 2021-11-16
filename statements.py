

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here
statement_generator("Welcome to the star system quiz", "*")
print()
statement_generator("Congratulations on completing the quiz, you are now more knowledgeable about the stars that light up our nights sky :)) ","!")
