""" e-Judge """
def main():
    """ Insert into... """
    number = int(input())
    lst = []
    for _ in range(number):
        text = input()
        lst.append(text)
    position = int(input())
    text = input()
    lst.insert(position, text)
    print(lst)
main()