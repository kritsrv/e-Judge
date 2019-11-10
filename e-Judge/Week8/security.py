""" e-Judge """
def main():
    """ Security """
    domain = input().split('/?')
    domain = domain[1].split('=')
    user = ''
    for i in domain[1]:
        if i == '&':
            break
        else:
            user += i
    password = domain[2]
    print(user)
    print(password)
main()
