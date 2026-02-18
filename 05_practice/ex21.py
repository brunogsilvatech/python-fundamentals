import datetime
def calculate_age(year_of_birth):
    actual_year = datetime.date.today().year
    return actual_year - year_of_birth
year = int(input("year of birth: "))
age = calculate_age(year)
print(age)