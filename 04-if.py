# operatory: == != > >= < <=
num1 = int(input('Enter a number: '))
if num1 > 0:
    print(f"{num1} is a positive number.")
elif num1 < 0:
    print(f"{num1} is a negative number.")
else:
    print("This is zero.")

if num1 % 2 == 0:
    print(f"{num1} is a even number.")
else:
    print(f"{num1} is a odd number.")
# if num1 % 2:
#     print(f"{num1} is a odd number.")
# else:
#     print(f"{num1} is a even number.")
num2 = 10
num3 = 10.0
num4 = 10
if num2 == num3:
    print("Same value")
if num2 is num3:
    print("Same object")
if num2 is not num3:
    print("Other object")
if num2 is num4:
    print("Same object")

# operatory: not and or

num5 = 0
if num5:
    print(f"{num5} is True")
else:
    print(f"{num5} is False")

age = int(input("What is your age? "))
gender = input("What is your gender M/F? ")
if gender == "M" or gender == "m":
    if age >= 18 and age < 65:
        print("Working age")
elif gender == "F" or gender == "f":
    if age >= 18 and age < 60:
        print("Working age")
else:
    print("Error!")

# if not False:
#     print("True")
# else:
#     print("False")