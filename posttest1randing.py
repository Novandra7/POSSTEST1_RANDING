# Nama : Awang Muhammad Novandra Arissaputra
# Kelas : Sistem Informasi A 2022

import os

def pemisah ():
    for i in range(len(ListKu)):
        if type (ListKu[i]) == int and list:
            listint.append(ListKu[i])
        else:
            listkosong.append(ListKu[i])

def partition(l, bwh, atas):
  pivot = l[bwh]
  pos_batas = bwh+1
  for j in range(bwh+1,atas):
    if l[j] < pivot:
      l[pos_batas],l[j]=l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
  return pos_batas

def quicksort(l, bwh, atas):
  if atas <= bwh:
    return
  q = partition(l, bwh, atas)
  quicksort(l, bwh, q-1)
  quicksort(l, q, atas)
  return l


ListKu = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
listkosong = []
listint = []

os.system('cls')
pemisah()
quicksort(listint, 0, len(listint)-1)
print("Setelah diurutkan : ", listint +  listkosong)
