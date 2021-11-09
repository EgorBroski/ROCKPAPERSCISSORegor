def start():
    """Teeme valik kellega mängime
    Tagastame m muutuja int formaadis

    :rtype: int
    """
    print("Kivi, Käärid, Paber")
    m=3
    while m not in [1,2]:
        try:
            m=int(input("Kellega mängime?\n1-inimesega\n2-robotiga\nKirjuta vastus:"))
        except:
            ValueError
    return m

def bot_vs_bot(v1:list,v2:list):
    """Robotite mäng
    Tagastame m muutuja int formaadis
    :param list v1: järjend esimese roboti jaoks
    :param list v2: järjend teise roboti jaoks
    
    """
    while True:
        print("Kas mängime? esc - välja, enter - mängime")
        if read_key()=='esc':
            break
        elif read_key()=='enter':
            p1=choice(v1)
            print("Esimene bot: ",p1)
            p2=choice(v2)
            print("Teine bot: ",p2)
            if p1==p2:
                print("Viik")
            if p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                print("Võitis 1")
            else:
                print("Võitis 2")
