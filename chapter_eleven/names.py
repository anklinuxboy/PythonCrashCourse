from name_func import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
    first = input("Please give me a first name: ")
    if first == 'q':
        break
    last = input("Please give a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")