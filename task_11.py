while True:
    number_a = input('Enter the number a >= 200:')
    if number_a.isdigit():
        number_a = int(number_a)
    else:
        print('a - Not a number')
        continue

    number_b = input('Enter the number b:')
    if number_b.isdigit():
        number_b = int(number_b)
    else:
        print('b - Not a number')
        continue

    if number_a <= 200:
        break
    else:
        print('Incorrect value. "a" must be less then or equal to 200')
        continue

sum_of_numbers = 0

if number_a > number_b:
    number_a, number_b = number_b, number_a

for number in range(number_a, number_b):
    sum_of_numbers += number

count = number_b - number_a
if count == 0:
    average = number_a
else:
    average = sum_of_numbers / (number_b - number_a)
print('Average:', average)
