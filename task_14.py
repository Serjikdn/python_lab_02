n = int(input('Enter a number greater than 1: '))
k = 0

while True:
    if 5 ** k > n:
        break
    k += 1

print('k =', k)
