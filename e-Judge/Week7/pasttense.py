""" e-Judge """
def main():
    """ Past Tense """
    text = input().split(" ")
    lst = []
    for i in text:
        if i == "is":
            lst.append('was')
        elif i == "are":
            lst.append('were')
        elif i == "Is":
            lst.append('Was')
        elif i == "Are":
            lst.append('Were')
        else:
            lst.append(i)
    print(*lst)
main()