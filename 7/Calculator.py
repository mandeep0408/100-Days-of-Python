num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
oper = input("Select your operator: ")
if oper == "+":
    print("The answer of ",num1,oper,num2,"will give you ",num1+num2)
elif oper == "-":
    print("The answer of ",num1,oper,num2,"will give you ",num1-num2)
elif oper == "*":
    print("The answer of ",num1,oper,num2,"will give you ",num1*num2)
elif oper == "/":
    print("The answer of ",num1,oper,num2,"will give you ",num1/num2)
