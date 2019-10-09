import sys, os
if(sys.platform == "win32"):
    clear = "cls"
else:
    clear  = "clear"
def IsPrime(number):
    r = pow(number,0.5)
    flag = True
    for i in range(2, int(r)+1):
        if(number % i == 0):
            flag = False
            break
    return flag
def Cicles(p):
    if(IsPrime(p)):
        l = []
        cont = 2
        while (cont<p):
            j = []
            for i in range(1, p):
                j.append(pow(cont%p,i%p)%p)
            flag = True
            for i in j:
                if(j.count(i) != 1):
                    flag = False
            if(flag):
                l.append(cont)
            cont +=1
        return l
def ErrorCatch():
    n = input("Try again?[Y|N]\n>>> ")
    if(n.lower() == 'y'):
        return True
    elif(n.lower() == 'n'):
        return False
    else:
        os.system(clear)
        return ErrorCatch()
def Main():
    while True:
        os.system(clear)
        try:
            print("\t\tCyclical Number Generator v0.1\n\t\t\tpor Zeta Hoffman")
            n = int(input("Enter a Prime Number\n>>> "))
            cicles = Cicles(n)
            print("The generators os cycles of {} are {}".format(n,cicles))
            input("Press \'Enter\' to continue . . . ")
        except:
            print("You should be enter a number")
            if(ErrorCatch()):
                pass
            else:
                break
Main()