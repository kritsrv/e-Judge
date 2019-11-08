""" e-Judge """
def main():
    """ Sort 2 """
    lst = []
    lst_2 = []
    for _ in range(10):
        number = int(input())
        lst.append(number)
    for _ in range(10):
        mi_n = min(lst)
        lst_2.append(mi_n)
        lst.remove(mi_n)
    print(lst_2)
main()