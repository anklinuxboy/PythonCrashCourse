banner_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banner_users:
    print(f"{user.title()}, you can post a response if you wish")

x = 42
y = 100
if x >= 42 and y <= 100:
    print("True")

alien_color = "green"
if alien_color == "green":
    print("5 points")
else:
    print("10 points")

age = 10
if age < 2:
    print("Baby!")
elif age >= 2 and age < 4:
    print("Toddler")
elif age >= 4 and age < 13:
    print("Kid")
elif age >= 13:
    print("Elder")