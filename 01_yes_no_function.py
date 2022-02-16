from pickle import FALSE


def yes_no(question):
    valid = False
    while not valid:
        response = input("have u played before").lower()

        yes = ["yes", "y", "ye"]
        no = ["no", "n"]

        # If they say yes, output 'program continues'
        if response in yes:
            response = "yes"
            return response


        elif response in no:
            response = "no"
            return response

        # If they say no, output 'program instructions'
        else:
            print("Please answer yes / no")