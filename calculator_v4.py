# Newest version, can't handle parentheses. Please input with spaces. 

operations = ["**", "*", "/", "//", "+", "-"]

def calculate(num1, operation, num2):
    if operation == "+": return num1 + num2
    if operation == "-": return num1 - num2
    if operation == "*": return num1 * num2
    if operation == "/": return num1 / num2
    if operation == "//": return num1 // num2
    if operation == "**": return num1 ** num2
    
calc = input("Enter calculation: ")
calc = calc.split(" ")
for i in range(len(calc)):
    if calc[i].replace('.','',1).isdigit():
        calc[i] = float(calc[i])

done = False

while not done:
    for i in range(len(calc)):
        if len(calc) == 1:
            done = True
        elif calc[i] in operations:
            if "**" in calc:
                if calc[i] == "**":
                    calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                    break
            elif "*" in calc or "/" in calc or "//" in calc:
                if calc[i] == "*" or calc[i] == "/" or calc[i] == "//":
                    calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                    break
            elif "+" in calc or "-" in calc:
                if calc[i] == "+" or calc[i] == "-":
                    calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                    break

print(round(calc[0], 3))