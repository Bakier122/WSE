first_list = [1, True, "Hello"]
for i in first_list:
    print(i, end="\t")
print(first_list)

numbers = [34, 89, 22, 10, 89, -2, 67, 87, 90]
print(numbers)
# print(numbers[0])
# print(numbers[1])
# print(numbers[-1])
# print(numbers[-2])
numbers[0] = 1
numbers[-1] = 1000
print(numbers)
numbers.append(56)
print(numbers)
numbers.insert(1, 21)
print(numbers)
numbers.pop()
print(numbers)
numbers.remove(89)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(sum(numbers))
sum = 0
for i in numbers:
    sum += i
print(sum)

order_numbers = list(range(0, 41, 2))
print(order_numbers)
print(len(order_numbers))