import math

first = int(input("First number: "))
second = int(input("First number: "))
third = int(input("First number: "))
fourth = int(input("First number: "))

number_list = [first, second, third, fourth]
temp_list = []

for number in number_list:
    temp_list.append(math.cos(number))

print(temp_list)
result = min(temp_list)
print('Min value: ', result)
