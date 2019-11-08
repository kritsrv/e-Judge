""" e-Judge """
def main():
    """ Backspace """
    text = input()
    lst = []
    for i in text:
        if i == "<":
            lst.pop()
        else:
            lst.append(i)
    print(*lst, sep="")
main()