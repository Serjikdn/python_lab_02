def discount_calculation(sum):
    if sum > 1000:
        print('Discount 5%')
        return sum * 0.05
    elif sum > 500:
        print('Discount 3%')
        return sum * 0.03
    else:
        print('No discount')
        return 0


purchase_amount = float(input("Enter the purchase amount: "))
print('Result:', discount_calculation(purchase_amount), 'uah')