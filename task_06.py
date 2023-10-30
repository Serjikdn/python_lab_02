import math

side_a = int(input('Enter side a: '))
side_b = int(input('Enter side b: '))

S = side_b / 4 * math.sqrt(4 * pow(side_a, 2) - pow(side_b, 2))

print('S = ', S)
