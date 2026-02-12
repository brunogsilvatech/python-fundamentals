def calculate_age(year_of_birth, current_year):
    return current_year - year_of_birth
year = int(input("which year were you born?: "))
age = calculate_age(year, 2026)
print("you are", age, "years old")