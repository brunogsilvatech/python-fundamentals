def calculate_age(current_year, year_of_birth):
    return current_year - year_of_birth
year = int(input("Which year were you born? :"))
age = calculate_age(2026, year)
if age > 18:
    print("You are an adult")
else:
    print("You are a minor")