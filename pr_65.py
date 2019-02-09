# coding=utf-8

"""
Závěrečný úkol pro předmět: Úvod do Programování.
Zadání úkolu: Dány dvě posloupnisti čísel. Nalezení jejich průniku (společné prvky)
Vypracovala: Kristýna Měchurová, rok: 2019
"""

import random
#definování funkcí
def listofrandomnum (number, a, b):
    """ Vytvoří list náhodných celých čísel.
        Vstup:  number - počet čísel v řetězci
                a, b  - interval náhodných čísel
                (a: minimální hodnota intervalu
                 b: maximální hodnota intervalu)
        Výstup: list náhodných čísel.
                """
    list =[]
    for i in range(number):
        randnum=random.randint(a,b)
        list.append(randnum)
    return list

def intersection (list1, list2):
    """ Průnik dvou listů obsahujících celá čísla.
        Vstup:  list1,list2 - list celých čísel
        Výstup: průnik vstupů ve formátu list
    """
    list1=listofint(list1)
    list2 = listofint(list2)
    result=[]
    for i in list1:
        if i in list2:
            result.append(i)
    return (list(set(result))) #odstranění duplicit z průniku

def listofint (listofnum):
    """Ošetření list obsahuje pouze celá čísla
      Vstup: list
      Výstup: list obsahující pouze celá čísla"""

    if all(isinstance(i, int) for i in listofnum)==True:
        return listofnum
    else:
        print ("List neobsahuje pouze celá čísla")
        quit (1)

#spouštění funkcí
list1= listofrandomnum(10,5,20)
list2= listofrandomnum(10,5,20)
print (list1)
print (list2)
print ("Průnik:",intersection(list1,list2))