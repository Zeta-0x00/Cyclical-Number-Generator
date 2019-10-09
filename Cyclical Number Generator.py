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
def Cicles(p,bFlag):
    if(IsPrime(p)):
        l = []
        cont = 2
        while (cont<p):
            j = []
            flag = True
            for i in range(1, p):
                if(pow(cont%p,i%p)%p in j):
                    flag = False
                else:
                    j.append(pow(cont%p,i%p)%p)
            if(flag):
                if(bFlag):
                    print(cont)
                l.append(cont)
            cont += 1
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
            print("\t\tCyclical Number Generator v0.2\n\t\t\tby Zeta Hoffman")
            n = int(input("Enter a Prime Number\n>>> "))
            cicles = Cicles(n,True)
            print("The generators os cycles of {} are {}".format(n,cicles))
            input("Press \'Enter\' to continue . . . ")
        except:
            print("You should be enter a number")
            if(ErrorCatch()):
                pass
            else:
                break
Main()