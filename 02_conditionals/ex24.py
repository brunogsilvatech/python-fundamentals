number = int(input("Choose a number:"))
if number % 3 == 0 and number % 5 == 0:
    print("Mutiple of 3 and 5")
elif number % 5 == 0:
    print("Multiple of 5")
elif number % 3 == 0:
    print("Multiple of 3")
else:
    print("Not a multiple of 3 or 5")