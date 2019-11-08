""" e-Judge """
def main():
    """ Music List """
    music = input().split(", ")
    lst = []
    lst_compare = []
    for i in music:
        if i.upper() in lst_compare:
            pass
        else:
            lst.append(i)
            lst_compare.append(i.upper())
    lst.sort(key=len, reverse=True)
    for i in range(len(lst)):
        print("%d.%s" % (i+1, lst[i]), end="\n")
main()