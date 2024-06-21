locations = open('locations.txt', 'r', encoding="utf-8").read().split('\n')
# print(locations)
value = 0
for i in locations:
    if i[0] == 'W':
        value += 1
print("W:",value)

for i in locations:
    if i[0] == 'Ś':
        print(i, end=" ")