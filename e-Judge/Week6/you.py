""" e-Judge """
def main(text):
    """ You """
    result = you(text)
    print(result)

def you(txt):
    """ + You """
    txt += " You" + ", " + txt + " You" + ", " + txt + " You" \
        + ", " + txt + " You" + ", " + txt + " You"
    all_txt = txt + "\n" + txt + "\n" + txt + "\n" + txt + "\n" \
        + txt + "\n" + txt + "\n" + txt + "\n" + txt + "\n" + txt + "\n" + txt
    return all_txt
main(input())