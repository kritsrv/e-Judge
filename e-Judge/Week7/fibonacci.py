""" e-Judge """
def main():
    """ Fibonacci """
    number = int(input())
    lst = [0, 1]
    answer = 0
    if number == 0:
        print(lst[0])
    elif number == 1:
        print(lst[1])
    else:
        for i in range(2, number+1):
            answer += lst[i-2] + lst[i-1]
            lst.append(answer)
            answer = 0
        print(lst[number])
main()