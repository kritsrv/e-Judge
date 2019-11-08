""" e-Judge """
import math as m
def main(amount):
    """ isPrime """
    for _ in range(amount):
        number = int(input())
        print(is_prime(number))
 
def is_prime(number):
    """ Check_Prime """
    if number > 3:
        p_number = "Yes"
        for i in range(2, int(m.sqrt(number))+1):
            if number % i != 0:
                pass
            else:
                p_number = "No"
        return p_number
    elif number == 2 or number == 3:
        return "Yes"
    else:
        return "No"
main(int(input()))