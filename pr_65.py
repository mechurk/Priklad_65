# coding=utf-8

"""
Závěrečný úkol pro předmět: Úvod do Programování.
Zadání úkolu: Dány dvě posloupnisti čísel. Nalezení jejich průniku (společné prvky)
Vypracovala: Kristýna Měchurová, rok: 2019
"""

import random


# definování funkcí

def fromtxttolist(text):
    """Z textového souboru vytvoří list
    Vstup: textový soubor
    Výstup: list celých čísel"""
    try:
        text_file = open(text, "r")
        lines = text_file.read().split(",")
        result = list(map(int, lines))
        print(result)
        text_file.close()
        return (result)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error")
        raise


def listofrandomnum(number, a, b):
    """ Vytvoří list náhodných celých čísel.
        Vstup:  number - počet čísel v řetězci
                a, b  - interval náhodných čísel
                (a: minimální hodnota intervalu
                 b: maximální hodnota intervalu)
        Výstup: list náhodných čísel.
                """
    list = []
    for i in range(number):
        randnum = random.randint(a, b)
        list.append(randnum)
    return list


def intersection(list1, list2):
    """ Průnik dvou listů obsahujících celá čísla.
        Vstup:  list1,list2 - list celých čísel
        Výstup: průnik vstupů ve formátu list
    """

    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return (list(set(result)))  # odstranění duplicit z průniku


def savetotxt(result):
    """uloží list do textového dokumentu
    Vstup: list duplicitních hodnot
    Výstup: textový soubor s názvem result_65.txt"""
    print(result)
    final_count = str(len(result))
    final_result = str(result)
    final_result = final_result.replace("[", "")
    final_result = final_result.replace("]", "")
    text_file_output = open("result_65.txt", "w")
    text_file_output.write("Průnik:\n")
    text_file_output.write(final_result + "\n")

    text_file_output.close()


# spouštění funkcí
list1 = fromtxttolist("test_1.txt")
list2 = fromtxttolist("test_2.txt")
print(list1)
print(list2)
result = intersection(list1, list2)
savetotxt(result)
