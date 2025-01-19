operations = ["^", "*", "/", "%", "+", "-"]

def calculate(num1, operation, num2):
    if operation == "+": return num1 + num2
    if operation == "-": return num1 - num2
    if operation == "*": return num1 * num2
    if operation == "/":
        if num1 % num2 == 0: return int(num1 / num2)
        else: return num1 / num2
    if operation == "^": return num1 ** num2
    if operation == "%": return num1 % num2

while True:    
    calc = input()
    if calc == "": break
    calclist = []
    calcnum = ""
    for i in range(len(calc)):
        if calc[i].isdigit(): 
            calcnum += calc[i]
            done = False
        elif calc[i] == ".":
            if calcnum.isdigit() and calc[i+1].isdigit():
                calcnum += calc[i]
            done = False
        elif calc[i] in operations:
            calclist.append(calcnum)
            calcnum = ""
            calclist.append(calc[i])
            done = False
        else:
            print("Not a valid calculation")
            done = 0
            break
    calclist.append(calcnum)
    calc = calclist
    for i in range(len(calc)):
        if calc[i].replace('.', '', 1).isdigit():
            if "." in calc[i]: calc[i] = float(calc[i])
            else: calc[i] = int(calc[i])

    while not done:
        for i in range(len(calc)):
            if len(calc) == 1:
                done = True
            elif calc[i] in operations:
                if "^" in calc:
                    if calc[i] == "^":
                        calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                        break
                elif "*" in calc or "/" in calc or "%" in calc:
                    if calc[i] == "*" or calc[i] == "/" or calc[i] == "%":
                        calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                        break
                elif "+" in calc or "-" in calc:
                    if calc[i] == "+" or calc[i] == "-":
                        calc[i-1:i+2] = [calculate(calc[i-1], calc[i], calc[i+1])]
                        break

    if done == True:
        print(round(calc[0], 10))