""" e-Judge """
def main():
    """ GCD """
    number = int(input())
    number_2 = int(input())
    gcd = 1
    if number != 0 and number_2 != 0:
        for i in range(2, max(number, number_2)+1):
            if number % i == 0 and number_2 % i == 0:
                gcd = i
        print(gcd)
    else:
        if number == 0:
            print(number_2)
        else:
            print(number) 
main()