def function_checkage(age):
    if age>= 18:
        return "Adult"
    else:
        return "Minor"
x = int(input("How old are you: "))
result = function_checkage(x)
print(result)