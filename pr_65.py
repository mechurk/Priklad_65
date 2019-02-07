# coding=utf-8
import random

def listofrandomnum (number, a, b):
    list =[]
    for i in range(number):
        randnum=random.randint(a,b)
        list.append(randnum)
    return list

def intersection (list1, list2):
    result=[]
    for i in list1:
        if i in list2:
            result.append(i)
    return (list(set(result)))

list1= listofrandomnum(100,10,110)
list2= listofrandomnum(100,10,110)
print (list1)
print (list2)
print (intersection(list1,list2))