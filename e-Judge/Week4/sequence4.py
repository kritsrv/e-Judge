""" e-Judge """
def main():
    """ Sequence 4 """
    size = int(input())
    for i in range(-(size//2), (size//2)+1):
        for j in range(-(size//2), (size//2)+1):
            box = abs(j) + ((size+1)//2)
            if i == 0:
                new_i = size//2
            else:
                new_i = (size//2)-abs(i)
            print(box-new_i, end=" ")
        print()
main()