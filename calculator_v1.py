operations = ["^", "*", "/", "+", "-"]
calculation = input("Enter calculation: ")

def add(term1, term2):
    return term1 + term2
def subtract(term1, term2):
    return term1 - term2 
def multiply(factor1, factor2):
    return factor1 * factor2
def divide(numerator, denominator):
    return numerator / denominator
def exponentiate(base, exponent):
    return base ** exponent

valid = False
for character in calculation:
    if character.isnumeric() or character in operations:
      valid = True
    else: 
        valid = False
        break

if valid:
    if "+" in calculation:
        numbers = calculation.split("+")
        print(add(int(numbers[0]), int(numbers[1])))
    if "-" in calculation:
        numbers = calculation.split("-")
        print(subtract(int(numbers[0]), int(numbers[1])))
    if "*" in calculation:
        numbers = calculation.split("*")
        print(multiply(int(numbers[0]), int(numbers[1])))
    if "/" in calculation:
        numbers = calculation.split("/")
        print(divide(int(numbers[0]), int(numbers[1])))
    if "^" in calculation:
        numbers = calculation.split("^")
        print(exponentiate(int(numbers[0]), int(numbers[1]))) 
else:
    print("That's not a valid calculation.")