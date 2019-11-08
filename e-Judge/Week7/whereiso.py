""" e-Judge """
def main():
    """ Where is O? """
    text = input().lower()
    located = 0
    if "o" not in text:
        print("There is no O here")
    else:
        for i in text:
            located += 1
            if i == "o":
                print("O is at %d" % located)
                break
            else:
                continue
main()