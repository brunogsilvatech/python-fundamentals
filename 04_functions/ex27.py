def is_even(number):
    return not number % 2
number = int(input("Choose a number:"))
result = is_even(number)
print(result)