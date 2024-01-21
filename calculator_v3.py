operations = ["**", "*", "/", "+", "-"]
calc = input("Enter calculation: ")
calc = calc.split(" ")

for i in range(len(calc)):
    if calc[i].isnumeric():
        calc[i] = int(calc[i])

pos = 0
new = ""
pre = ""

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

for item in calc:
    if new != "":
        pre = new
    if item in operations:
        for operation in operations:
            if operation in calc:
                if pre == "":
                    new = [calc[pos-1], item, calc[pos+1]]
                else:
                    new = [pre, item, calc[pos+1]]
                new = calculate(new[0], new[1], new[2])
    pos += 1

print(new)