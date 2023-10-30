while True:
    number_a = input('Enter the number a:')
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

    if number_a < number_b:
        break
    else:
        print('Incorrect value. "b" must be greater then or equal to 200')
        continue


value = number_a
sum_numbers = 0
while value < number_b:
    print(value)
    value += 1
    sum_numbers += value

print('Sum:', sum_numbers)
