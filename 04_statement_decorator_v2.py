# function goes here
import re


def decorator(text, decoration, lines):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    if lines == "3":
        print(decoration * text_length)
        print(statement)
        print(decoration * text_length)
        return ""

    elif lines == "1":
        print(statement)
        return ""
    else:
        return ""


# main routine

heading = decorator("Welcome to my Game", "~", "3")
print()
print()
heading = decorator("Welcome to my Game", "~", "1")
