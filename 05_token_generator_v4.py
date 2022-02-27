import random

# main routine
STARTING_BALANCE = 100

balance = STARTING_BALANCE
# testing loop to generate 20 tokens
for item in range(0,100):
    chosen_num = random.randint(1,100)
    
    
    # adjusts balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
        print("unicorn")
    elif 5 < chosen_num <= 36:
        chosen_num == "donkey"
        balance -= 1
        print("donkey")
    else:
        chosen = "horse / zebra"
        balance -= 0.5
        print(random("horse", "zebra")

# output
print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))