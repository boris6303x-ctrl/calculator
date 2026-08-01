print("Calculator 1.0")
# simple calculator for my IT lessons
def main():
    expression = input("Enter an expression: ")
    if validation(expression):
        expression_list = parser(expression)
        multdiv_list = multdiv(expression_list)
        result = addsub(multdiv_list)
        print(f"Result: {result}")
    else:
        print("ValueError: input must be an expression.")


def validation(expression):
    NUMBERS = "0123456789"
    FUNCTIONS = "+-*/"
    is_valid = True
    no_space_expression = expression.replace(" ","")
    for i in range(len(no_space_expression)):
        if no_space_expression[i] not in NUMBERS and no_space_expression[i] not in FUNCTIONS:
            return False
    return is_valid

def multdiv(expression_list):
    pass

def addsub(multdiv_list):
    pass

def parser(expression):
    pass

# 4 + 3 * 2 - 8 / 2
# 4+6-4
# 6



# 123
# if (x.isdigit() and y.isdigit()):
#     x = int(x)
#     y = int(y)
#     if f == 1:
#         print(result_str, x + y)
#     elif f == 2:
#         print(result_str, x - y)
#     elif f == 3:
#         print(result_str, x * y)
#     elif f == 4:
#         if y == 0:
#             print("ZeroDivisionError: can't divide by 0")
#         elif x / y == int(x / y):
#             print(result_str, int(x / y))
#         else:
#             print(result_str, x / y)
#     else:
#         print("Error: Invalid function number")
# else:
#     print("TypeError: Invalid input")

if __name__ == "__main__":
    main()
