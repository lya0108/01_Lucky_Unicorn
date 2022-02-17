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

# Main Routine 
instructions = yes_no("Have u played this game before? ")
print("you chose {}".format(instructions))
print()
fun = yes_no("Having fun? ")
if fun == "no":
    print("{} is incorrect".format(fun))
elif fun == "yes":
    print("You said {} to having fun".format(fun))

    
