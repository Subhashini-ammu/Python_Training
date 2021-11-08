print("\n!!!!! Program to find the greatest of 3 numbers using function !!!!\n")

num1 = input("Enter the first number : ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number : ")


def maximum(num1, num2, num3):

    if num1.isnumeric() and num2.isnumeric() and num3.isnumeric():

        if (num1 > num2) and (num1 > num3):
            print("\n", num1, "is the greater number than", num2, "and", num3)

        elif num2 > num1 and num2 > num3:
            print("\n", num2, "is the greater number than", num1, "and", num3)

        elif num3 > num1 and num3 > num2:
            print("\n", num3, "is the greater number than", num1, "and", num2)

        elif num1 == num2 and num1 == num3:
            print("\nNumbers", num1, ",", num2, "and", num3, " are equal")

        elif num1 == num2 and num1 > num3:
            print("\nNumbers", num1, "and", num2, " are equal and greater than", num3)

        elif num3 == num1 and num3 > num2:
            print("\nNumbers", num1, "and", num3, " are equal and greater than", num2)

        elif num2 == num3 and num2 > num1:
            print("\nNumbers", num2, "and", num3, " are equal and greater than", num1)

    else:
        print("\nError!!!! Please enter valid numbers.")


maximum(num1, num2, num3)
