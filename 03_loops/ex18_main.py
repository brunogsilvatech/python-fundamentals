def check_age(age):
    if age<= 10:
        return "Child"
    elif age< 18:
        return "Teen"
    else:
        return "Adult"
x = int(input("How old are you: "))
result = check_age(x)
print(result)