number = int(input("Choose a number "))
if number ==0:
    print("zero")
elif number >0:
    if number %2==0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    if number %2==0:
        print("Negative even")
    else:
        print("Negative odd")