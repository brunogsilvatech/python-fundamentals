def get_parity(number):
  if number %2==0:
    return "even"
  else:
    return "odd"
number = int(input("choose a number:"))
result = get_parity(number)
print(result)