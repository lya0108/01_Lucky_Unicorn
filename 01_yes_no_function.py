def yes_no(question):
    valid = False
    while not valid:
        
        response = input("have u played before").lower()

        # If they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response


        elif response == "no" or response == "n":
            response = "no"
            return response

        # If they say no, output 'program instructions'
        else:
            print("Please answer yes / no")