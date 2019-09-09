#!/usr/bin/env python3
# coding: utf-8

import random

a = []
k = 5 # просто начальное значение, может быть любым
for r in range(5): # 6 строк
    a.append([]) # создаем пустую строку
    for c in range(15): # в каждой строке - 10 элементов
        a[r].append(k) # добавляем очередной элемент в строку
        k += 1 # увеличиваем значение счетчика
 
#for r in a:
   # print(r)




b = []
for y in range(6): # 6 строк
    b.append([]) # создаем пустую строку
    for d in range(10): # в каждой строке - 10 элементов
        b[y].append(random.randint(10, 100))

#for y in b:
    #print(y)



n = int(input()) 
ac = []
for i in range(n):
    ac.append([int(j) for j in input().split()])
print(ac)