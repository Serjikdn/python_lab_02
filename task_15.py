n = int(input('Enter number n:'))

for i in range(n):
    if i * i > n:
        print(i * i)
        break
