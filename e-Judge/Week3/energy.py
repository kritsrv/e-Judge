""" e-Judge """
def main():
    """ Energy """
    kilo = float(input())
    pork_energy = int(input())
    metre = kilo * 1000
    energy = pork_energy * 10
    number_pork = metre // energy
    if metre % energy == 0:
        print("%d" % number_pork)
    else:
        number_pork += 1
        print("%d" % number_pork)
main()