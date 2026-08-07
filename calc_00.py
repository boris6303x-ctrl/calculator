NUMBERS = "0123456789"
FUNCTIONS = "+-*/"

print("Calculator 1.0")
def main():
    expression = input("Enter an expression: ")
    if validation(expression):
        expression_list = parser(expression)
        multdiv_list = multdiv(expression_list)
        if multdiv_list == "ZeroDivisionError":
            print("ZeroDivisionError: cannot divide by zero")
            return
        result = addsub(multdiv_list)
        print(f"Result: {result}")
    else:
        print("ValueError: input must be not empty and an expression.")

def validation(expression):
    no_space_expression = expression.replace(" ","")
    if no_space_expression == "":
        return False
    else:
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
                    return "ZeroDivisionError"
                else:
                    result_list.append(int(last_number / next_number))
            idx += 1
        else:
            result_list.append(expression_list[idx])
        idx += 1
    return result_list

def addsub(multdiv_list):
    result = int(multdiv_list[0])
    idx = 1
    while idx < len(multdiv_list):
        if multdiv_list[idx] == "+":
            result += int(multdiv_list[idx+1])
        elif multdiv_list[idx] == "-":
            result -= int(multdiv_list[idx+1])
        idx += 2
    return result

def parser(expression):
    return expression.split(" ")


if __name__ == "__main__":
    main()
