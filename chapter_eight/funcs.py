def greet_user(username):
    """Displays a simple greeting"""
    print(f"hello {username.title()}!")

greet_user('porter')

def favorite_book(title):
    """Displays a favorite book"""
    print(f"My favorite book is {title.title()}")

favorite_book('sherlock holmes')

def make_shirt(text, size='L'):
    print(f"The T shirt made will be {size} big and have the message '{text}' on it")

make_shirt(text='I love Python')

def cities(city, country="USA"):
    print(f"{city} is in {country}")

def get_formatted_name(first_name, last_name, middle_name=''):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

name = get_formatted_name('harry', 'potter')
print(name)