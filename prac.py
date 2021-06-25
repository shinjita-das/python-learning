def calc(input1, input2, operator):
    value = None
    # Start here
    # if else
    # math operators
    # how to compare strings in python
    if operator == "+":
        value = input1 + input2
    elif operator == "-":
        value = input1 - input2
    elif operator == "*":
        value = input1 * input2
    elif operator == "/":
        value = input1 / input2
    else:
        print("Invalid operator")
        # End here
    return value


def print_this(name):
    print('Hey ' + name)
    # return 0


option = 1
while option != 'exit':
    print("Enter your first value")
    number1 = int(input())
    print("Enter your second value")
    number2 = int(input())
    print("Enter you operator")
    op = input()
    print(calc(number1, number2, op))
    # print_this("Mat")
    option = input("Type exit if you want to exit:")


