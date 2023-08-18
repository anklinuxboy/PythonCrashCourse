message = input("Tell me something, and I will repeat back to you: ")

print(message)

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\n You're tall enough to ride")
else:
    print("\n ")

car = input("what kind of rental car would you like?: ")

print(f"Let me see if I can find you a {car.title()}")

num = int(input("Enter a number: "))

if num % 10 == 0:
    print("is a multiple of 10")
else:
    print("not")
