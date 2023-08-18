from pathlib import Path

path = Path('guests.txt')

guests = ''

i = 10

while i > 0:
    guest = input('Enter guest name: ')
    guests += guest + '\n'
    i -= 1

path.write_text(guests)

