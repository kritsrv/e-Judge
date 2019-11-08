""" e-Judge """
def main():
    """ Month """
    number = int(input())
    month = "January  February March    April    May      \
June     July     August   SeptemberOctober  November December "
    print(month[(number-1)*9:number*9])
main()