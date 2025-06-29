def sum_calc(a, b):
   sum = a+b
   print(sum)

def diff_calc(a, b):
   diff = a - b
   print(diff)

def prod_calc(a, b):
   prod = a*b
   print(prod)

def div_calc(a, b):
   div = a/b
   print(div)

print("welcome to calculator")

num1 = int(input("enter 1st no. = "))
operation = input("enter the operation = ")
num2 = int (input("enter 2nd no. = "))

if (operation == "+"):
   sum_calc(num1, num2)

if (operation == "-"):
   diff_calc(num1, num2)

if (operation == "*"):
   prod_calc(num1, num2)

if (operation == "/"):
    if (num2 == 0):
        print("error")
    else: 
        div_calc(num1, num2)
      
   
