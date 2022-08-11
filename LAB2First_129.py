import os
import time
while True :
    os.system("cls")
    Value = int(input("Enter Value 1-12 : "))
    start = 1
    if Value == 0:
        print("You Select Exit.")
        time.sleep(1)
        exit()
    elif Value < 1 or Value > 12:
        print("..!..You enter invalid value please enter value again in range 1 - 12..! ")
        time.sleep(3)
        continue
    else:        
        print("\n\nWhile Loop start = ",start)
        while start <= 12 :  
            print(Value," X ",start," = ",Value * start)
            start = start+1 
        print("\n\nFor Loop start = ",start)
        for start in range(1,13) :  
            print(Value," X ",start," = ",Value * start)
            start = start+1
        time.sleep(3)  

