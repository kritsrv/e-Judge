""" e-Judge """
def main():
    """ SWAP """
    lst = []
    for _ in range(5):
        text = input()
        lst.append(text)
    lst[0], lst[4] = lst[4], lst[0]
    print(lst)
main()