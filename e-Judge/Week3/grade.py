""" e-Judge """
def main():
    """ Grade """
    score = float(input())
    if 100 >= score >= 80:
        print("A")
    elif 80 > score >= 75:
        print("B+")
    elif 75 > score >= 70:
        print("B")
    elif 70 > score >= 65:
        print("C+")
    elif 65 > score >= 60:
        print("C")
    elif 60 > score >= 55:
        print("D+")
    elif 55 > score >= 50:
        print("D")
    elif 0 <= score < 50:
        print("F")
    else:
        print("Invalid Score.")
main()