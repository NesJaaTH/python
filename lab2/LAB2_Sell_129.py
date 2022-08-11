from threading import local
import time
import calendar
import os

def Menu(order):
    
    localtime = time.asctime(time.localtime(time.time()))
    Water = 7
    Coke = 10
    Milk = 35
    Sandwich = 25
    order = order
    itw = 0
    itc = 0
    itm = 0
    itsw = 0
    os.system("cls")
    while True:
        print("MADBOY-SHOP \t",  localtime,"\tOrder ID =", order)

        print("Menu","\t\tPrice")
        print("Water\t\t", Water,"\tBaht\nCoke\t\t", Coke,"\tBaht\nMilk\t\t", Milk,"\tBaht\nSandwich\t", Sandwich,"\tBaht")
        Seitem = int(input("Select Item 1 - 4 or Go to receipt sum price enter 0 (Zero) = "))
        if Seitem == 0:
            print("tset")
            os.system("cls")
            sellout(order,localtime,itw,itc,itm,itsw)
        elif Seitem == 1:
            seitemW = int(input("Please input number = "))
            itw += seitemW
            os.system("cls")
        elif Seitem == 2:
            seitemC = int(input("Please input number = "))
            itc += seitemC
            os.system("cls")
        elif Seitem == 3:
            seitemM = int(input("Please input number = "))
            itm += seitemM
            os.system("cls")
        elif Seitem == 4:
            seitemSW = int(input("Please input number = "))
            itsw += seitemSW
            os.system("cls")

def sellout(order,time,itw,itc,itm,itsw):
    time = time
    order = order
    itw = itw
    itwsm = 1
    itc = itc
    itcsm = 1
    itm = itm
    itmsm = 1
    itsw = itsw
    itswsm = 1
    sellcout = 1
    sumsell = 1
    vat = 1.89
    sellprice = 100
    print(time,"\nOrder ID = ",order)
    print("ITEM :\n\t Water\t\t X ",itw,"\t",itwsm,"Baht","\n\t Coke\t\t X ",itc,"\t",itcsm,"Baht","\n\t Milk\t\t X ",itm,"\t",itmsm,"Baht","\n\t Sandwich\t X ",itsw,"\t",itswsm,"Baht")
    print("\n\t sum", sellcout," Item","\t", sumsell," Baht")
    print("\n\t Vat 7%\t",vat,"\t\t",sellprice,"Baht")
    neworder = input("\t New Order [N]")
    neworder = neworder.upper()
    if neworder == "N":
        order += 1
        Menu(order)

if __name__ == '__main__':
    order = 1000
    Menu(order)