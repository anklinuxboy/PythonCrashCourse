from pathlib import Path

path = Path('learning_programming.txt')

f_string = ''

lines = path.read_text().splitlines()

for line in lines:
    f_string += line + ' '

f_string = f_string.replace('python', 'rust')

path.write_text(f_string)

print(f_string)
