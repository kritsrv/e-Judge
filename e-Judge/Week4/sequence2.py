""" e-Judge """
def main():
    """ Sequence 2 """
    triangle = int(input())
    for row in range(1, triangle+1):
        print(" " * (triangle-row), end="")
        for col in range(1, row+1):
            col = str(col)
            print(col, end=" ")
        print()
main()