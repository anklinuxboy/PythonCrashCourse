guests = ["richard feynman", "leonardo da vinci", "roger federer"]

print(f"Hello {guests[0].title()}, you're invited for dinner.")
print(f"Hello {guests[1].title()}, you're invited for dinner.")
print(f"Hello {guests[2].title()}, you're invited for dinner.")

print(f"Hello, {guests[1].title()} can't make it")

guests[1] = "oppenheimer"

guests.insert(0, "rafael nadal")
guests.insert(2, "harry potter")
guests.append("sherlock holmes")

print(guests)

print("Can only invite two people")

guests.pop(0)
guests.pop(1)
guests.pop(1)
guests.pop()

print(guests)

del guests[0]
del guests[0]

print(guests)