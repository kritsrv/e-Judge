""" e-Judge """
def main():
    """ Matrix """
    row = int(input())
    colomn = int(input())
    lst = []
    for _ in range(row):
        for _ in range(colomn):
            number = input()
            lst.append(number)
        print(*lst, end="\n")
        lst.clear()
main()