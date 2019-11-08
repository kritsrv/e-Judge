""" e-Judge """
def main():
    """ How long """
    text = input()
    text_02 = input()
    number_text = ord(text.upper())
    number_text_02 = ord(text_02.upper())
    submission = abs(number_text-number_text_02)
    print(submission)
main()