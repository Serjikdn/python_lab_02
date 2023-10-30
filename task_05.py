import math

first = int(input("First number: "))
second = int(input("First number: "))
third = int(input("First number: "))


number_list = [first, second, third]
temp_list = []

for number in number_list:
    temp_list.append(math.sin(number))

print(temp_list)
result = max(temp_list)
print('Max value: ', result)
