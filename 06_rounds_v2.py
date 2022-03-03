import random

# get balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print("~~~ Round #{} ~~~".format(rounds_played))
    
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