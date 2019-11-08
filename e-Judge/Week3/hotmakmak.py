""" e-Judge """
def main():
    """ Hot Mak Mak """
    temp = int(input())
    if 27 <= temp <= 35:
        print("hot")
    elif 36 <= temp <= 40:
        print("hot mak mak")
    elif temp >= 41:
        print("die nae nae")
    else:
        print("cold")
main()