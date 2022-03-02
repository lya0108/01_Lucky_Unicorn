import random

# main routine
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 20 tokens
for item in range(0,10):
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

# output
print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
print()