""" e-Judge """
def main():
    """ Password Generator Checker """
    password = input()
    sum_ = 0
    if (len(password) == 6) and (password[0:3].isupper() and password[3:].islower()):
        for i in password:
            sum_ += ord(i)
        print('Your password is : ' + password + str(sum_))
    else:
        print('Password is not secure or invalid')
main()
