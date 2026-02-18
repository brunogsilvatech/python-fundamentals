number = int(input("Choose a number: "))
if number ==0:
    print("Zero")
elif number >0:
    if number %2==0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    if number %2==0:
        print("Negative Even")
    else:
        print("Negative Odd")