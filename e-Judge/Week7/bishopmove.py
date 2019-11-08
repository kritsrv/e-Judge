""" e-Judge """
def main():
    """ Bishop Move """
    start = input()
    stop = input()
    if abs(int(start[1])-int(stop[1])) == abs(int(start[4])-int(stop[4])):
        print('Yes')
    else:
        print('No')
main()