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

def yes_no(question):

    valid = False
    while not valid:
        
        yes = ["yes", "y", "ye"]
        no = ["no", "n", "nah"]

        response = input(question).lower()

        if response in yes:
            response = "yes"
            return response

        elif response in no:
            response = "no"
            return response

        else:
            print("Please type yes / no ")
            print()

def instructions():
    decorator("How To Play", "~", "3")
    print()
    print("Rules")
    print()
    return ""

# Main Routine 
played_before = yes_no("Have u played this game before? ")

if played_before == "no":
    instructions()

print("pogram continues")

