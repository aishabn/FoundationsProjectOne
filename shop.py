####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Frosted"
signature_flavors = ["tuna", "salmon", "red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print ("Our menu: ")
    for k,v in menu.items():
        print ( '"' + k + '" ' + "(KD " + str(v) + ")" )


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for i in original_flavors:
        print ('"'+i+'"')


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for i in signature_flavors:
        print ('"'+i+'"')


def is_valid_order(order):
    
    if order in menu:
        return True

    elif order in original_flavors:
        return True

    elif order in signature_flavors:
        return True

    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    item = input("What's your order? (Enter exact spelling of the item you want. Type 'Exit' to end your order.)")

    while item.lower() != "exit":

        if is_valid_order(item) == True:
            order_list.append(item)
        else:
            print ("Invalid item")

        item = input()

    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        return True

    else:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    
    for i in order_list:

        if i in menu:
            total += menu[i]

        elif i in original_flavors:
            total += original_price

        elif i in signature_flavors:
            total += signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for i in order_list:
        print ('- '+ i)

    print()

    price = get_total_price(order_list)
    print ("That'll be KD " + str(price))

    if accept_credit_card(price):
        print ("This order is eligible for credit card payment.")
    else:
        print ("This order is not eligible for credit card payment.")

    print ("Thank you for shopping at " + cupcake_shop_name)
