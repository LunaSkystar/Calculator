operations = ["**", "*", "/", "+", "-"]
calculation = input("Enter calculation: ")

def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    if operation == "**":
        return num1 ** num2

for operation in operations:
    if operation in calculation:
        numbers = calculation.split(operation)
        print(calculate(int(numbers[0]), operation, int(numbers[1])))
        break