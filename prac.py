
def calc(input1, input2,operator):
       value = None
       if operator == "+":
              value= number1+number2
       elif operator == "-":
              value= number1-number2
       elif operator == "*":
              value = number1 ** number2
       elif operator == "/":
              value = number1 // number2
       else: print ("Inva lid")

              return value

print("Enter your first value")
number1 = int(input())
print("Enter your second value")
number2 = int(input())
print("Enter you operator")
op= input()
print(calc(number1, number2,op))