print("\nProgram to calculate when the user will turn 100 years based on user age using functions\n ")


def year():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return 100 - age + 2021


print('\nHi, you will turn 100 years old in the year', str(year()))