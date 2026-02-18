number = int(input("Choose a number "))
if number ==0:
    print("Zero")
else:
    if number >0:
        sign = "Positive"
    else:
        sign = "Negative"
    if number %2==0:
        parity = "Even"
    else:
        parity = "Odd"
    print(sign,parity)