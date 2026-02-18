number = int(input("Chose a number :"))
if number ==0:
    print("Zero")
elif number >0 and number %2==0:
    print("Positive even")
elif number >0 and number %2!=0:
    print("Positive odd")
elif number <0 and number %2==0:
    print("Negative even")
else:
    print("Negative odd")