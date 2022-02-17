def yes_no(question):
    valid = False
    while not valid:
        
        yes = ["yes", "y", "ye"]
        no = ["no", "n"]
        
        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response in yes:
            return "yes"


        elif response in no:
            return "no"

        # If they say no, output 'program instructions'
        else:
            print()
            print("Please answer yes / no")

show_instructions = yes_no("have you played before ")