price = [6.90, 7.50, 8.50, 9.50, 9.20, 8.90, 7.90, 7.60, 7.50, 7.43, 7.40, 7.12, 6.99, 6.87, 6.90, 6.86, 6.70, 6.90, 7.20, 7.10, 7.30, 7.03, 7.09, 7.12, 6.98, 6.89, 7.50, 8.50, 8.20, 7.90, 7.70, 7.60, 7.50, 7.43, 7.40, 7.12]
avg_price = sum(price) / len(price)
print("Average price:", round(avg_price, 2))
print("Max price:", max(price))
print("Min price:", min(price))

# ver. 1:
# avg_price_first_year = sum(price[0:12]) / 12
# print("Average first year price:", round(avg_price_first_year, 2))
# print("Max price - first year:", max(price[0:12]))
# print("Min price - first year:", min(price[0:12]))
# avg_price_second_year = sum(price[12:24]) / 12
# print("Average second year price:", round(avg_price_second_year, 2))
# print("Max price - second year:", max(price[12:24]))
# print("Min price - second year:", min(price[12:24]))
# avg_price_third_year = sum(price[24:36]) / 12
# print("Average third year price:", round(avg_price_third_year, 2))
# print("Max price - third year:", max(price[24:36]))
# print("Min price - third year:", min(price[24:36]))

# ver. 2:
# sum1 = 0
# min1, max1 = price[0], price[0]
# for i in range(0, 12):
#     sum1 += price[i]
#     if price[i] > max1:
#         max1 = price[i]
#     if price[i] < min1:
#         min1 = price[i]
# print("Average price - first year:", round(sum1/12, 2))
# sum2 = 0
# for i in range(12, 24):
#     sum2 += price[i]
# print("Average price - second year:", round(sum2/12, 2))
# sum3 = 0
# for i in range(24, 36):
#     sum3 += price[i]
# print("Average price - third year:", round(sum3/12, 2))

# ver. 3:
for i in range(3):
    print(f"Average - {i+1} year price:", round(sum(price[i*12:(i+1)*12])/12, 2))
    print(f"Max price - {i+1} year:", max(price[i*12:(i+1)*12]))
    print(f"Min price - {i+1} year:", min(price[i*12:(i+1)*12]))