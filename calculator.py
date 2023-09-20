def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


a, b = map(float, input("Enter two number: ").split())
print(" 1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exit\n")
choice = int(input("Enter your choice: "))

while choice != 5:
    if choice == 1:
        print(add(a, b))
        break

    if choice == 2:
        print(subtract(a, b))
        break

    if choice == 3:
        print(multiply(a, b))
        break

    if choice == 4:
        print(divide(a, b))
        break