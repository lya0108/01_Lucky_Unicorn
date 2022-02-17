from tokenize import maybe


def yes_no():

    valid = False
    while not valid:
        
        yes = ["yes", "y", "ye"]
        no = ["no", "n", "nah"]

        response = input("have you played before ").lower()

        if response in yes:
            return "yes"

        elif response in no:
            return "no"

        else:
            print("Please type yes / no ")
            print()

answer = yes_no()
print("you chose", answer)