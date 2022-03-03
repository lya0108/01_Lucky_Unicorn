import random

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
    print("Choose a starting amount (minimum $1, maximum $10")
    print()
    print("Then press <Enter> to play. You will get either a horse, a zebra, a donkey, a mule, a foal, a unicorn or a golden unicorn")
    print()
    print("It costs $1 per round. Depending on your prize you might win some money back. Here's the payout amounts...")
    print("Horse: $0.50 (balance decreases by $$0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1)")
    print("Mule: -$99.00 (balance decreases by $100)")
    print("Foal: $3.00 (balance increases by $2)")
    print("Unicorn: $5.00 (balance increases by $4)")
    print("Golden Unicorn: $201.00 (balance increases by $200)")
    print()
    print()
    return ""

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

# Main Routine 
played_before = yes_no("Have u played this game before? ")

if played_before == "no":
    instructions()
print()

# ask how much they wish to play with
how_much = num_check("How much would you like play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    decorator("Round #{}".format(rounds_played), "~", "1")
    
    chosen_num = random.randint(1,10000)
    
    
    # adjusts balance                                                                                                                                                                                
    if 1 <= chosen_num <= 500:
        chosen = "unicorn"
        balance += 4
    elif 3603 < chosen_num <= 4103:
        chosen = "foal"
        balance += 2
    elif 500 < chosen_num <= 3600:
        chosen = "donkey"
        balance -= 1
    elif 3600 < chosen_num <= 3602:
        chosen = "mule"
        balance -= 100
    elif 3602 < chosen_num <= 3603:
        chosen = "golden unicorn"
        balance += 200
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5
    
    print("you got a {}. your balance is ${:.2f}".format(chosen, balance))
    
    if balance < 1:
        play_again = "xxx"
        print("Sorry you are broke")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit ")

# output
print()
print("Final Balance: ${:.2f}".format(balance))
print()