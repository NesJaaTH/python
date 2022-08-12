from threading import local
import time
import calendar
import os


def Menu(order):
    
    localtime = time.asctime(time.localtime(time.time()))
    itembaht = [7,10,35,25]
    itemcount = [0,0,0,0]
    itembuycount = [0,0,0,0]

    os.system("cls")

    while True:
        print("MADBOY-SHOP \t",  localtime,"\tOrder ID =", order)
        print("Menu","\t\tPrice")
        print("1.Water\t\t", itembaht[0],"\tBaht\n2.Coke\t\t", itembaht[1],"\tBaht\n3.Milk\t\t", itembaht[2],"\tBaht\n4.Sandwich\t", itembaht[3],"\tBaht")
        Seitem = int(input("Select Item 1 - 4 or Go to receipt sum price enter 0 (Zero) = "))
        if Seitem == 0:
            os.system("cls")
            itembuycount[0] = itemcount[0] * itembaht[0]
            itembuycount[1] = itemcount[1] * itembaht[1]
            itembuycount[2] = itemcount[2] * itembaht[2]
            itembuycount[3] = itemcount[3] * itembaht[3]
            sellout(order,localtime,itemcount,itembuycount)
        elif Seitem == 1:
            seitemW = int(input("Please input number = "))
            itemcount[0] += seitemW
            os.system("cls")
        elif Seitem == 2:
            seitemC = int(input("Please input number = "))
            itemcount[1] += seitemC
            os.system("cls")
        elif Seitem == 3:
            seitemM = int(input("Please input number = "))
            itemcount[2] += seitemM
            os.system("cls")
        elif Seitem == 4:
            seitemSW = int(input("Please input number = "))
            itemcount[3] += seitemSW
            os.system("cls")
        else:
            os.system("cls")
            print("ERROR \tPlease Select Number 1 - 4 not input letter")
            time.sleep(3)
            os.system("cls")
            
def sellout(order,times,itemcount,itembuycount):
    sellcount = itemcount[0] + itemcount[1] + itemcount[2] + itemcount[3]
    sumsell = itembuycount[0] + itembuycount[1] + itembuycount[2] + itembuycount[3]
    pvat = sumsell + ( sumsell * 7 ) / 100
    vat = pvat - sumsell
    while True:
        print(times,"\nOrder ID = ",order)
        print("ITEM :\n\t Water\t\t X ",itemcount[0],"\t",itembuycount[0],"Baht","\n\t Coke\t\t X ",itemcount[1],"\t",itembuycount[1],"Baht","\n\t Milk\t\t X ",itemcount[2],"\t",itembuycount[2],"Baht","\n\t Sandwich\t X ",itemcount[3],"\t",itembuycount[3],"Baht")
        print("\n\t sum", sellcount," Item","\t", sumsell," Baht")
        print("\n\t Vat 7%\t",format(vat,".2f"),"\t\t",pvat,"Baht")
        neworder = input("\t New Order [N]")
        neworder = neworder.upper()
        if neworder == "N":
            order += 1
            Menu(order)
        elif neworder != "N" :
            os.system("cls")
            print("ERROR Please input N to Neworder")
            time.sleep(3)
            os.system("cls")

if __name__ == '__main__':
    order = 1000
    Menu(order)