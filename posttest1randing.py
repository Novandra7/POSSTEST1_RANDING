# Nama : Awang Muhammad Novandra Arissaputra
# Kelas : Sistem Informasi A 2022

def seperate(item):
  global result
  result = []
  for variable in item:
      if isinstance(variable, list):
          for i in variable:
              if isinstance(i, list):
                  for a in i :
                      # print(int(a))
                      result.append (int (a))
              elif isinstance(i, int) :
                  # print(i)
                  result.append (i)
      else :
          # print(variable)
          result.append(variable)
  urutin(result)

def urutin (array):
      if len(array) > 1:
        r = len(array)//2
        l = array[:r]
        m = array[r:]
        urutin(l)
        urutin(m)
        i = j = k = 0
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = m[j]
                j += 1
            k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(m):
            array[k] = m[j]
            j += 1
            k += 1

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
seperate(variable)
print("sebelum diurutkan : ",variable)
print("setelah diurutkan : ",result)
