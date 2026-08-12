def calculate_checkout(cart_total, shipping_speed, speed, shipping):
    if speed == "express":
        shipping = 20
    elif speed == "overnight":
        shipping = 35
    elif speed == "standard" and cart_total >=100:
        shipping = 0
    elif speed == "standard":
        shipping = 10
    else:
        print("ERROR please input valid variables")
    cart_total = float(input("enter your cart total: "))
    shipping_speed = input("enter shipping speed you want (standard, express, overnight): ")
    def calculate_checkout(cart_total, shipping_speed, speed, shipping):
    if speed == "express":
        shipping = 20
    elif speed == "overnight":
        shipping = 35
    elif speed == "standand" and cart_total >=100:
        shipping = 0
    elif speed == "standard":
        shipping = 10
    else:
        print("ERROR please input valid variables")
    cart_total = float(input("enter your cart total: "))
    shipping_speed = input("enter shipping speed you want (standard, express, overnight): ")
    total_cost = cart_total + shipping_speed
    print(total_cost)







   




