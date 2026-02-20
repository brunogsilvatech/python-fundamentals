def is_even(number):
    if number %2==0:
        return "Even"
    return "Odd"
number = int(input("Choose a number:"))
result = is_even(number)
print(result)