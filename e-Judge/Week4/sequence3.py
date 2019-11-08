""" e-Judge """
def main():
    """ Sequence 3 """
    size = int(input())
    for i in range(1, size+1):
        space = " " * abs(size-i)
        box = space + str(int("1"*i)**2)
        print(box, end="\n")
    for j in range(size-1, 0, -1):
        space = " " * abs(size-j)
        box = space + str(int("1"*j)**2)
        print(box, end="\n")
    print()
main()