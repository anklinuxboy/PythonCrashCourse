alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
alien_0['speed'] = 'fast'

del alien_0['points']
print(alien_0)

favorites_languages = {
    'ankit': ['python', 'rust', 'kotlin'],
    'user_two': ['python', 'R'],
    'guido': 'python',
}

for k in favorites_languages.values():
    print(k)

# print(favorites_languages)

person = {
    'first_name': 'harry',
    'last_name': 'potter',
    'age': 24,
    'city': 'New York'
}

for key, value in person.items():
    print(f"{key}: {value}")

rivers = {
    'nile': 'egypt',
    'ganges': 'india',
    'amazon': 'brazil'
}

for k, v in rivers.items():
    print(f"{k} runs through {v}")