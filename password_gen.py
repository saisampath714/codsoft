import random


def generate(n):
    chars = "!@#$%^&*()abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    password = ""

    for i in range(n):
        password += random.choice(chars)

    return password


n = int(input("Enter the length of password: "))
print(generate(n))