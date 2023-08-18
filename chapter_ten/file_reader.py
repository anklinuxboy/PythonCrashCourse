from pathlib import Path

path = Path('./digits.txt')
contents = path.read_text()

pi_string = ''
lines = contents.splitlines()

for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday: ")

if birthday in pi_string:
    print("Birthday in pi")
else:
    print("Birthday not in pi")