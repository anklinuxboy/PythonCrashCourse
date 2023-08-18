users = ["admin", "roger", "kit", "jocelyn"]
# users = []

if len(users) == 0:
    print("Need to find some users!")

for user in users:
    if user == "admin":
        print("Hello Admin, would you like a status report?")
    else:
        print(f"Hello {user.title()}, welcome back")

current_users = [user.lower() for user in users]
new_users = ["ROGER", "ankit", "sherlock", "Kit"]

for user in new_users:
    if user.lower() in current_users:
        print(f"{user} is already taken. Please pick a different name")