""" e-Judge """
def main():
    """ Sort """
    lst = []
    for _ in range(10):
        number = int(input())
        lst.append(number)
    lst.sort()
    print(lst)
main()