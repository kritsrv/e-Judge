""" e-Judge """
def main():
    """ PPAP """
    level = 0
    while level != 4:
        lyrics = input().lower()
        if lyrics == "pen" and level == 0:
            level += 1
        elif lyrics == "pineapple" and level == 1:
            level += 1
        elif lyrics == "apple" and level == 2:
            level += 1
        elif lyrics == "pen" and level == 3:
            level += 1
        else:
            if lyrics == "pen":
                level = 1
                print("Wrong lyrics!")
            else:
                level = 0
                print("Wrong lyrics!")
    print("Correct lyrics!")
main()