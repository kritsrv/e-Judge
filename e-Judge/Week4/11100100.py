""" e-Judge """
def main():
    """ 11100100 """
    number = input()
    text = ""
    for i in range(len(number)):
        if number[i] == "0" or number[i] == "1":
            text += number[i]
    print(text)
main()