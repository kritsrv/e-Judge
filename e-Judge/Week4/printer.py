""" e-Judge """
def main():
    """ Printer """
    printer = input()
    ma_xprice = 0
    mi_nprice = 99999
    while printer != "END":
        if "ALL-IN-ONE" in printer:
            printer = printer.split(",")
            price = int(printer[1])
            name = printer[0]
            if price > ma_xprice:
                ma_xprice = price
                name_printer1 = name
            if price < mi_nprice:
                mi_nprice = price
                name_printer2 = name
        printer = input()
    if ma_xprice == 0 and mi_nprice == 99999:
        print("Not found")
    else:
        print(name_printer1)
        print(name_printer2)
main()