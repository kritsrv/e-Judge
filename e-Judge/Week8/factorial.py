""" e-Judge """
def main():
    """ Factorial-ial-ial !!! """
    number = int(input())
    mark = len(input()) # !
    answer = 1
    for i in range(number, 0, -mark):
        answer *= i
    print(answer)
main()
