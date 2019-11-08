""" e-Judge """
def main():
    """ Simon says """
    number = int(input())
    for _ in range(number):
        text = input()
        if text[0:10] == "Simon says":
            print(text[11:])
main()