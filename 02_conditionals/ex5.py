name = input("what is your name? ")
year_birth = int(input("Which year were you born? "))
age = 2026 - year_birth
print("Nice to meet you,", name, )
print("You are", age, "years-old" )
if age >= 18:
    print("You are an adult.")
else:
    print("You are under age")