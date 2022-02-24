# functions here
def num_check(question, low, high):
    error = "Please enter a whole number between 1 - 10\n"

    valid = False
    while not valid:
        try:

            # ask the question
            response = int(input(question))

            # if the amount is too low / high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)
        
        except ValueError:
            print(error)

# main routine
how_much = num_check("How much would you like play with? ", 0, 10)

print("You are spending ${}\n".format(how_much))