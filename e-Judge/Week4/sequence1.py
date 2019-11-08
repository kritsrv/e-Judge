""" e-Judge """
def main():
    """ Sequence 1 """
    square = int(input())
    for row in range(1, square+1):
        for col in range(row, square+row):
            if col % square == 0:
                print(col, end=" ")
            else:
                print(col % square, end=" ")
        print()
main()