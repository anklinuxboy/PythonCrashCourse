from pizza import make_pizza as mp

def city_country(city = '', country = ''):
    """Returns a formatted String"""
    return f"{city.title()}, {country.title()}"

print(city_country('boston', 'usa'))
print(city_country('giza', 'egypt'))
print(city_country('new delhi', 'india'))

def make_album(artist_name = '', album_name = ''):
    """Returns a dictionary"""
    return {'name': artist_name.title(), 'album': album_name.title()}

artists = []
album_one = make_album('glass animals', 'dreamland')
album_two = make_album('taylor swift', '1989')
album_three = make_album('backstreet boys', "backstreet's back")

artists.append(album_one)
artists.append(album_two)
artists.append(album_three)

for artist in artists:
    print(f"{artist['name']}, {artist['album']}")

mp.make_pizza(12, 'mushrooms', 'green peppers')

def make_sandwich(*items):
    print(items)

make_sandwich('tomato', 'onion', 'cucumber')