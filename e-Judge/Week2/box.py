""" e-Judge """
def main():
    """ The box """
    number_square = int(input())
    number_dokjun = "* " * number_square
    square = ((number_dokjun + "\n") * (number_square-1) + number_dokjun)
    print(square)
main()