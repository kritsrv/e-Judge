""" e-Judge """
def main():
    """ Word Game """
    text = input()
    score = 100
    for _ in range(20):
        answer = input()
        if answer == text:
            print("Correct!! You've %d points remaining." % score)
            break
        else:
            score -= 5
        if score == 0:
            print('Game Over!')
main()