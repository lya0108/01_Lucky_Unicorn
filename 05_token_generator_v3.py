import random

# main routine
tokens = ["unicorn", "horse", "horse", "zebra", "zebra", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 20 tokens
for item in range(0,100):
    chosen = random.choice(tokens)
    
    
    # adjusts balance
    if chosen == "unicorn":
        balance += 4
    
    elif chosen == "donkey":
        balance -= 1

    else:
        balance -= 0.5

# output
print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))