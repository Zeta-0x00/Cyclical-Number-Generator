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
            k = 1
            for i in range(1, p):
                k  = (k*cont)%p
                if(k in j):
                    flag = False
                    break
                else:
                    if(k != 1):
                        j.append(k)
            if(flag):
                l.append(cont)
                if(bFlag):
                    print(cont)
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
    Name()
    time.sleep(0.5)
    print("\n\n----------------------------------------------\n|Cyclical Number Generator v. 1.0            |\n|Elaborated by Daniel \'Zeta\' Hoffman         |\n|Developed solely with educational character | \n|\tfor the ITCR cryptography course     | \n----------------------------------------------")
    Pause()
def Name():
    print("\n\t-----------------------------------------------------------------------------------------------------------------------------\n\t $$$$$$\  $$\           $$\ $$\                    $$\       $$\   $$\                         $$\                           \n"
            "\t$$  __$$\ \__|          $$ |\__|                   $$ |      $$$\  $$ |                        $$ |                          \n"
            "\t$$ /  \__|$$\  $$$$$$$\ $$ |$$\  $$$$$$$\ $$$$$$\  $$ |      $$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  \n"
            "\t$$ |      $$ |$$  _____|$$ |$$ |$$  _____|\____$$\ $$ |      $$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ \n"
            "\t$$ |      $$ |$$ /      $$ |$$ |$$ /      $$$$$$$ |$$ |      $$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|\n"
            "\t$$ |  $$\ $$ |$$ |      $$ |$$ |$$ |     $$  __$$ |$$ |      $$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      \n"
            "\t\$$$$$$  |$$ |\$$$$$$$\ $$ |$$ |\$$$$$$$\\$$$$$$$ |$$ |      $$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      \n"
            " \t \______/ \__| \_______|\__|\__| \_______|\_______|\__|      \__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|      \n"
            "\t\t\t $$$$$$\                                                    $$\                         \n"
            "\t\t\t$$  __$$\                                                   $$ |                        \n"
            "\t\t\t$$ /  \__| $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  \n"
            "\t\t\t$$ |$$$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ \____$$\\_$$  _|  $$  __$$\ $$  __$$\ \n"
            "\t\t\t$$ |\_$$ |$$$$$$$$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|\n"
            "\t\t\t$$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |     $$  __$$ | $$ |$$\ $$ |  $$ |$$ |      \n"
            "\t\t\t\$$$$$$  |\$$$$$$$\ $$ |  $$ |\$$$$$$$\ $$ |     \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      \n"
             "\t\t\t \______/  \_______|\__|  \__| \_______|\__|      \_______|  \____/  \______/ \__|      \n"
              "\n\t----------------------------------------------------------------------------------------------------------------------------\n")
def Menu():
    Clean()
    Name()
    print("\tBy Zeta")
    time.sleep(0.4)
    n = input("\n\nSelect Any option\n1. Calculate a Cyclicals Numbers by\n2. Identify if the number is prime\n3. About this software\n0. Exit\n>>> ")
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
