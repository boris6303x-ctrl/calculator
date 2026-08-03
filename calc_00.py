NUMBERS = "0123456789"
FUNCTIONS = "+-*/"

print("Calculator 1.0")
# simple calculator for my IT lessons
def main():
    expression = input("Enter an expression: ")
    if validation(expression):
        expression_list = parser(expression)
        multdiv_list = multdiv(expression_list)
        if multdiv_list == "#DIV/0!":
            print("ZeroDivisionError: cannot divide by zero")
            exit()
        result = addsub(multdiv_list)
        print(f"Result: {result}")
    else:
        print("ValueError: input must be an expression.")

def validation(expression):
    no_space_expression = expression.replace(" ","")
    if no_space_expression[0].isdigit() and no_space_expression[len(no_space_expression)-1].isdigit():
        for i in range(len(no_space_expression)):
            if no_space_expression[i] not in NUMBERS and no_space_expression[i] not in FUNCTIONS:
                return False
        return True
    else:
        return False

def multdiv(expression_list):
    result_list = []
    idx = 0
    while idx < len(expression_list):
        if expression_list[idx] == "*" or expression_list[idx] == "/":
            last_number = int(result_list.pop(len(result_list)-1))
            next_number = int(expression_list[idx+1])
            if expression_list[idx] == "*":
                result_list.append(last_number * next_number)
            elif expression_list[idx] == "/":
                if next_number == 0:
                    return("#DIV/0!")
                elif last_number / next_number == int(last_number / next_number):
                    result_list.append(int(last_number / next_number))
                else:
                    result_list.append(last_number / next_number)
                idx += 1
        else:
            result_list.append(expression_list[idx])
        idx += 1
    return result_list

def addsub(multdiv_list):
    pass

def parser(expression):
    return expression.split(" ")

# 4 + 3 * 2 - 8 / 2
# 4+6-4
# 6



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
