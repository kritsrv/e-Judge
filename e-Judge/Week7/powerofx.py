""" e-Judge """
def main():
    """ Power of X """
    number = int(input())
    divide = number//2
    for i in range(1, divide+1):
        print((' ' * (i-1)) + "\\" + (" " * (number-(2*i)) + "/"))
    for j in range(divide, 0, -1):
        print((' ' * (j-1)) + "/" + (" " * (number-(2*j)) + "\\"))
main()