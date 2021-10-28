print("\n!!!!! Program to find the greatest of 3 numbers using function !!!!\n")

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number : "))


def max(num1, num2, num3):

    if (num1 > num2) and (num1 > num3):
        print("\n", num1, "is the greater number than", num2, "and", num3)

    elif (num2 > num1 and num2 > num3):
        print("\n", num2, "is the greater number than", num1, "and", num3)

    elif (num3 > num1 and num3 > num2):
        print("\n", num3, "is the greater number than", num1, "and", num2)

    elif (num1 == num2 or num1 == num3 or num2 == num3):
        print("\n Numbers",num1,"and",num2, " are equal and greater")

max(num1,num2,num3);