def calculate():
    try:
        n1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        n2 = float(input("Enter second number: "))
        
        if op == '+': print(n1 + n2)
        elif op == '-': print(n1 - n2)
        elif op == '*': print(n1 * n2)
        elif op == '/': print(n1 / n2 if n2 != 0 else "Error!")
        else: print("Invalid Operator")
    except ValueError:
        print("Invalid Number")

calculate()
