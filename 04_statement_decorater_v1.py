# function goes here
def decorator(text, decoration):

    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    text_length = len(statement)

    print(decoration * text_length)
    print(statement)
    print(decoration * text_length)

    return None


# main routine

heading = decorator("Welcome to my Game", "~")