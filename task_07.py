number_month = input('Enter number of month: ')

match number_month:
    case '1':
        month = 'January'
    case '2':
        month = 'February'
    case '3':
        month = 'March'
    case '4':
        month = 'April'
    case '5':
        month = 'May'
    case '6':
        month = 'June'
    case '7':
        month = 'July'
    case '8':
        month = 'Adjust'
    case '9':
        month = 'September'
    case '10':
        month = 'October'
    case '11':
        month = 'November'
    case '12':
        month = 'December'
    case _:
        month = 'not defined'

print(number_month, 'is', month)
