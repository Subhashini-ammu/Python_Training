
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))

if(num1>num2) and (num1>num3):
    print("\n",num1,"is greater than",num2,"and",num3)

elif(num2>num1 and num2>num3):
    print("\n",num2,"is greater than",num1,"and",num3)

else:
    print("\n",num3,"is greater than",num1,"and",num2)
