def main():
    a = float(raw_input('Enter value of A here: '))
    b = float(raw_input("Enter value for B here: "))
    c = float(raw_input("Enter Value for C here: "))

    t = float(raw_input("Enter T(C) here: "))
    pnot = 10**(a- (b/(t+c)))
    print pnot

while True:
    main()
    print '==============================='
