while True:
    number_a = input('Enter the number a:')
    if number_a.isdigit():
        number_a = int(number_a)
    else:
        print('a - Not a number')
        continue

    if 0 > number_a or number_a > 50:
        print('Incorrect value. 0 <= a <= 50')
        continue
    else:
        break
result = 0
for number in range(number_a, 50):
    result += pow(number, 2)
    print(number)
    print(result)

print(result)
