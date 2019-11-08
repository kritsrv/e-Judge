""" e-Judge """
def main():
    """ Jelly """
    value = input().split(" ")
    all_cut = 0
    for i in value:
        all_cut += cutting(int(i))
    print(all_cut)
 
def cutting(number):
    """ cut from n to 1 """
    count = 0
    while number > 1:
        number //= 2
        count += 1
    return count
 
main()