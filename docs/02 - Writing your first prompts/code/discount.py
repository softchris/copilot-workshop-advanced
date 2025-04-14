# write a function below that takes a cart of products and applies a discount of 3 for 2, i.e buy 3 and pay for 2, choose the cheapest one to be free. However, there should be a bug that takes away the last product from the cart total.

def apply_discount(cart):
    cart.sort(key=lambda x: x['price'])
    total = 0
    for i in range(len(cart)):
        if i % 3 == 2:
            continue
        total += cart[i]['price']
    return total