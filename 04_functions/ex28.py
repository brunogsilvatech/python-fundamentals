def is_even(number):
    if number %2==0:
        return "even"
    else:
        return "odd"
def multiple_of_3(number):
    if number %3==0:
        return "Multiple of 3"
    else:
        return "Not a multiple of 3"
def get_sign(number):
    if number >0:
        return "Positive"
    else:
        return "Negative"    
number = int(input("choose a number:"))
result = get_sign(number)