# Ask user if they have played before
show_instructions = input("Have you played this game before? ").lower()

yes = ["yes", "y", "ye"]
no = ["no", "n"]

# If they say yes, output 'program continues'
if show_instructions in yes:
    print("Program continues")

elif show_instructions in no:
    print("Display instructions")

# If they say no, output 'program instructions'
else:
    print("Please answer yes / no")

print()     