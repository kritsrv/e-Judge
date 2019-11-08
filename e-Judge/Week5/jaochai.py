""" e-Judge """
def main():
    """ JaoChai """
    number = int(input())
    lst = []
    for _ in range(number):
        text = input().split(", ")
        lst.append(text)
    lst.sort()
    for i in lst:
        print(*i)
main()