""" e-Judge """
def main():
    """ Get A """
    number_row = int(input())
    for row in range(1, number_row+1):
        if row == 1:
            print(" " * (number_row-row) + "A")
        elif row == number_row//2 + 1:
            print(" " * (number_row//2 - (number_row % 2 == 0)) +\
                 "A" * (number_row + (number_row % 2 == 0)))
        else:
            print(" " * (number_row-row) + "A" +\
                " " * ((row-1)*2-1) + "A")
main()