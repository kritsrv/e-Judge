""" e-Judge """
def main():
    """ Median """
    number = input().split(", ")
    lst = []
    answer = 0
    for i in number:
        new_number = float(i)
        lst.append(new_number)
        lst.sort()
    mid = len(lst)//2
    if len(lst) % 2 == 0:
        answer = (lst[mid-1] + lst[mid]) / 2
    else:
        answer = lst[mid]
    print('%.2f' % answer)
main()