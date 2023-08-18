try:
    print(5/0)
except ZeroDivisionError:
    print("Can't divide by zero")

while True:
    first_number = input('\n First Number')
    if first_number == 'q':
        break