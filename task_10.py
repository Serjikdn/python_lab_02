a = int(input('Enter A: '))
b = int(input('Enter B: '))

sum_integers = 0
for i in range(a, b + 1):
    sum_integers += pow(i, 2)

print(f"Sum of squares from A({a}) to B({b}):", sum_integers)
