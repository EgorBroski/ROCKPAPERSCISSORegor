from keyboard import*
from random import*
from My_module import*
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]

m=start()
if m==1:
    bot_vs_bot(v1,v2)
elif m==2:
    while 1:
        pass

while True:
    try:
        if read_key()=="k":
            print("Oli valitud kivi")
            break
    except:
        ValueError
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]
if m==1:
    while 1:
        print("Mängime")
        v=input()
        if v=="no":break
        if read_key()=="N": break
        p1=choice(v1)
        print("Esimene bot: ",p1)
        p2=choice(v2)
        print("Teine bot: ",p2)
        if p1==p2: print("Viik")
        if p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
            print("Võitis 1")
        else:
            print("Võitis 2")
