a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

arr = [a, b, c]
result = list(item for item in arr if 1 <= item <= 3)
print(f"Numbers belonging to the interval [1,3]: ", ", ".join(map(str, result)))
