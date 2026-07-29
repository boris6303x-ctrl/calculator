print("Calculator 1.0")
# simple calculator for my IT lessons

x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")
result_str = "Result: "

print("Function guide: 1 = Addition(+), 2 = Subtraction(-), 3 = Multiplication(*), 4 = Division(/)")
f = int(input("Enter function Nr.: "))

# 123
if (x.isdigit() and y.isdigit()):
    x = int(x)
    y = int(y)
    if f == 1:
        print(result_str, x + y)
    elif f == 2:
        print(result_str, x - y)
    elif f == 3:
        print(result_str, x * y)
    elif f == 4:
        if y == 0:
            print("ZeroDivisionError: can't divide by 0")
        elif x / y == int(x / y):
            print(result_str, int(x / y))
        else:
            print(result_str, x / y)
    else:
        print("Error: Invalid function number")
else:
    print("TypeError: Invalid input")
