places = ['machu picchu', 'pyramids of giza', 'bora bora', 'great wall of china', 'zion national park']

for place in places[:3]:
    print(place)

pizzas = ["margharita", "bbq chicken", "plain cheese"]
friend_pizzas = pizzas[:]

pizzas.append("pepperoni")
friend_pizzas.append("mushroom")

print(pizzas)
print(friend_pizzas)