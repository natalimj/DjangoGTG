def gtgVAT (x,n):
    return round(x+ (x*n/100.0), 2)


def calculatePrice (drink, quantity):
    if drink.type == "COFFEE":
        result= gtgVAT (float(drink.price) * float(quantity),20.0) 
    else :
        result = drink.price * quantity
    return result