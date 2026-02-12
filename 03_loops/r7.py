number = int(input("Choose a number: "))
if number >0:
    print("Positive")
elif number ==0:
    print("Zero")
else:
    print("Negative")
if number %2 == 0:
    print("Even")
else:
    print("Odd")