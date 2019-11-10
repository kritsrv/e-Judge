""" e-Judge """
def main():
    """ Prime n to m """
    start = int(input())
    stop = int(input())
    step = [-1, 1][start <= stop]
    count = 0
    for i in range(start, stop+step, step):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime and i >= 2:
            count += 1
    print(count)
main()
