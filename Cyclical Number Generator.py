import sys, os, time
if(sys.platform == "win32"):
    clear = "cls"
else:
    clear  = "clear"
def IsPrime(number):
    r = pow(number,0.5)
    for i in range(2, int(r)+1):
        if(number % i == 0):
            return False
    return True
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
        Clean()
        return ErrorCatch()
def Clean():
    os.system(clear)
def Pause():
    input("Press \'Enter\' to continue . . . ")
def Main(flag):    
    try:
        n = int(input("Enter a Prime Number\n>>> "))
        cicles = Cicles(n,flag)
        print("The generators os cycles of {} are {}".format(n,cicles))
        Pause()
    except:
        print("You should be enter a number")
        if(ErrorCatch()):
            return Main(getManer())
        else:
            return
def getManer():
    n = input("Would you like show the numbers during the process?[Y|N]\n>>> ")
    if(n.lower() == 'y'):
        return True
    elif(n.lower() == 'n'):
        return False
    else:
        return getManer()
def getNumber():
    try:
        n = int(input("Enter a number\n>>> "))
        return n
    except:
        print("Invalid char\nPlease enter only numbers")
        return getNumber()
def About():
    Clean()
    print("Cyclical Number Generator v. 0.3\nElaborated by Daniel \'Zeta\' Hoffman\nDeveloped solely with educational character for the ITCR cryptography course\nMIT research and education licensed work")
    Pause()
    
def Menu():
    Clean()
    print("\t ▄▄·  ▄· ▄▌ ▄▄· ▄▄▌  ▪   ▄▄·  ▄▄▄· ▄▄▌       ▐ ▄ ▄• ▄▌• ▌ ▄ ·. ▄▄▄▄· ▄▄▄ .▄▄▄       ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄·▄▄▄▄▄      ▄▄▄  \n"
          "\t▐█ ▌▪▐█▪██▌▐█ ▌▪██•  ██ ▐█ ▌▪▐█ ▀█ ██•      •█▌▐██▪██▌·██ ▐███▪▐█ ▀█▪▀▄.▀·▀▄ █·    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█•██  ▪     ▀▄ █·\n"
          "\t██ ▄▄▐█▌▐█▪██ ▄▄██▪  ▐█·██ ▄▄▄█▀▀█ ██▪      ▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▪▄▐▀▀▄     ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█ ▐█.▪ ▄█▀▄ ▐▀▀▄ \n"
          "\t▐███▌ ▐█▀·.▐███▌▐█▌▐▌▐█▌▐███▌▐█ ▪▐▌▐█▌▐▌    ██▐█▌▐█▄█▌██ ██▌▐█▌██▄▪▐█▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌▐█▌·▐█▌.▐▌▐█•█▌\n"
          "\t·▀▀▀   ▀ • ·▀▀▀ .▀▀▀ ▀▀▀·▀▀▀  ▀  ▀ .▀▀▀     ▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀▀▀ .▀  ▀    ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀ ▀▀▀  ▀█▄▀▪.▀  ▀\n")
    print("\tBy Zeta")
    n = input("\nSelect Any option\n1. Calculate a Cyclicals Numbers by\n2. Identify if the number is prime\n3. About this software\n0. Exit\n>>> ")
    if(n == '0'):
        sys.exit()
    elif(n == '1'):
        Main(getManer())
    elif(n == '2'):
        if(IsPrime(getNumber())):
            print("Is a Prime Number")
            Pause()
        else:
            print("Is not a Prime Number")
            Pause()
    elif(n == '3'):
        About()
    else:
        print("Invalid parameter")
        time.sleep(2)
        return Menu()
    return Menu()
Menu()