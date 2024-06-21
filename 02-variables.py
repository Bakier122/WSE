# v1 = 3
# print(v1, type(v1))
# v1 = "qwerty"
# print(v1, type(v1))

# typy zmiennych
v1 = 1
v2 = 1.0
v3 = "1"
v4 = True #False
print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))

# adresy zmiennych
v5 = 25
v6 = 25
print("v5:", v5, id(v5))
print("v6:", v6, id(v6))
v6 = 66
print(f"v6: {v6}", id(v6))
v6 = 25
print(f"v6: {v6}", id(v6))
v7 = 66
print(f"v7: {v7}", id(v7))

# przypisanie funkcji do zmiennej
# x = print
# x("#"+"F"*6)
# print = "F"
# x("#"+print*6)

my_important_number = 7 # min = 7   myimportnum = 7
user_id = 7 # user_identifier = 7

number_1 = 256
number_2 = 0x100
number_3 = 0o400
number_4 = 0b100000000
print(number_1, number_2, number_3, number_4)

number_1 = 100.
number_2 = 0.10
number_3 = .10
number_4 = 1e2
print(number_1, number_2, number_3, number_4)
