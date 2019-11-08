""" e-Judge """
def main(number):
    """ f(g(x)) g(f(x)) """
    fog_x = fogx(number)
    gof_x = gofx(number)
    print("%.2f" % fog_x)
    print("%.2f" % gof_x)
 
def fogx(number):
    """ f๐g(x) """
    g_number = number/2 + 1
    f_number = g_number**2 + g_number*2 + 1
    return f_number
 
def gofx(number):
    """ g๐f(x) """
    f_number = number**2 + number*2 + 1
    g_number = f_number/2 +1
    return g_number
 
main(int(input()))