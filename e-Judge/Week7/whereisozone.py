""" e-Judge """
def main():
    """ Where is Ozone """
    number = int(input())
    print(" " * (number-1) + "*")
    new_number = number-1
    for i in range(1, new_number+1):
        print((" " * (new_number-i)) + "*"\
         + (" " * (i-1)) + "*" + (" " * (i-1)) + "*" + (" " * (i-1)))
    print(" " * (number-1) + "*")
    print(" " * (number-1) + "*")
    print(" " * (number-1) + "*")
main()