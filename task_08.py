first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))

numbers_list = [first, second, third]
counter = 0

for number in numbers_list:
    if number > 0:
        counter += 1

print('Positive numbers is', counter)
