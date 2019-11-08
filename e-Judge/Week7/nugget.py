""" e-Judge """
def main():
    """ Nugget """
    buy = int(input())
    free = int(input())
    want = int(input())
    price = int(input())
    pack = buy + free
    amount = want // pack
    cost = amount*buy*price
    get = amount*pack
    remain = want - get
    if remain >= buy:
        get += pack
        cost += buy*price
    else:
        get += remain
        cost += remain*price
    print("Pay: %d" % cost)
    print("Get: %d" % get)
main()