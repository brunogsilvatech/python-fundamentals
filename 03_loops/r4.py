def function_number(a):
    if a >0:
        print("Positive")
    elif a ==0:
        print("Zero")
    else:
        print("negative")
x = int(input("Choose a number? "))
result = x
function_number(x)