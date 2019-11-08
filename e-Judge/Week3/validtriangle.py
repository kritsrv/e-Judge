""" e-Judge """
def main():
    """ Valid Triangle """
    side_a = float(input())
    side_b = float(input())
    side_c = float(input())
    if side_a + side_b > side_c:
        if side_b + side_c > side_a:
            if side_a + side_c > side_b:
                print("Triangle is valid.")
            else:
                print("Triangle is not valid.")
        else:
            print("Triangle is not valid.")
    else:
        print("Triangle is not valid.")
main()