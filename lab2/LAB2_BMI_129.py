import os
import math
import time

def bmic():
    os.system("cls")
    tits = "\t\t\t\tbody mass index calculation"
    print(tits.upper())
    weight = float(input("\n\t\t\t\t  Input weight Number = "))
    height = float(input("\n\t\t\t\t  Input height Number = "))

    sum = weight / (math.pow(height / 100,2))
    if sum >= 30.0:
        while True:
            print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
            print('\t\t\t\t\t      อ้วนมาก')
            exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
            if exitbmi == 1:
                bmic()
            elif exitbmi == 2:
                break;
            else:
                os.system("cls")
                print("Error")
                time.sleep(3)
    elif sum >= 25.0:
        while True:
            print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
            print('\t\t\t\t\t       อ้วน')
            exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
            if exitbmi == 1:
                bmic()
            elif exitbmi == 2:
                break;
            else:
                os.system("cls")
                print("Error")
                time.sleep(3)
    elif sum >= 23.0:
            while True:
                print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
                print('\t\t\t\t\tน้ำหนักเกินมาตรฐาน')
                exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
                if exitbmi == 1:
                    bmic()
                elif exitbmi == 2:
                    break;
                else:
                    os.system("cls")
                    print("Error")
                    time.sleep(3)
    elif sum >= 18.5:
            while True:
                print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
                print('\t\t\t\t\tน้ำหนักสมส่วน')
                exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
                if exitbmi == 1:
                    bmic()
                elif exitbmi == 2:
                    break;
                else:
                    print("Error")
                    time.sleep(3)
    elif sum <= 18.5:
            while True:
                print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
                print('\t\t\t\t\tน้ำหนักต่ำกว่าเกณฑ์')
 
                exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
                if exitbmi == 1:
                    bmic()
                elif exitbmi == 2:
                    break;
                else:
                    os.system("cls")
                    print("Error")
                    time.sleep(3)
    else:
            while True:
                print("\n\t\t\t\t\tค่า BMI = ",format(sum,".2f"))
                print('\t\t\t\t\t\tอ้วนมาก')

                exitbmi = int(input("\n\t\t\t\t   Please 1. Continue 2.EXIT = "))
                if exitbmi == 1:
                    bmic()
                elif exitbmi == 2:
                    break;
                else:
                    os.system("cls")
                    print("Error")
                    time.sleep(3)
        
        


if __name__ == '__main__':
    bmic()
