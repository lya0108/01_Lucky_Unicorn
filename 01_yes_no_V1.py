# Ask user if they have played before
show_instructions = input("Have you played this game before? ").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "no":
    print("Display instructions")

# If they say no, output 'program instructions'
else:
    print("Please answer yes / no")

print()