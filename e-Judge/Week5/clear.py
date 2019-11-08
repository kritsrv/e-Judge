""" e-Judge """
def main():
    """ Clear """
    text = input()
    lst = []
    while text != "END":
        lst.append(text)
        if text.lower() == "clear":
            lst.clear()
        text = input()
    if lst == []:
        print("list is empty")
    else:
        for i in range(len(lst)):
            print(lst[i])
main()