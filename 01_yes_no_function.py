from winsound import PlaySound


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
    print("=== How To Play ===")
    print()
    print("Rules")
    print()
    return ""

# Main Routine 
played_before = yes_no("Have u played this game before? ")

if played_before == "no":
    instructions()

print("pogram continues")