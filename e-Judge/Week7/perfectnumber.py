""" e-Judge """
def main():
    """ Perfect Number """
    number = int(input())
    result = 0
    txt = ""
    lst = []
    for i in range(1, number+1):
        if (number % i == 0) and (i != number):
            lst.append(i)
    for i in lst:
        result += i
        if i == lst[-1]:
            txt += str(i) + " = " + str(result)
        else:
            txt += str(i) + " + "
    print(txt)
    if result == number:
        print("Yes!!! This is a perfect number.")
    else:
        print("Oops!!! This is not a perfect number.")
main()