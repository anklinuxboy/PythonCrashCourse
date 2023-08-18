def make_pizza(size, *toppings):
    """Print the lists of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with following toppings:")
    for topping in toppings:
        print(topping)