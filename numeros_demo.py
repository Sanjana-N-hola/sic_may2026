import sys
import numeros

n = int(input('Enter size of first list:'))
print('Enter list1 elements:')
list1 = []
for i in range(n):
    ele = int(input())
    list1.append(ele)

m = int(input('Enter size of second list:'))
print('Enter list2 elements:')
list2 = []
for i in range(m):
    ele = int(input())
    list2.append(ele)




missing_numbers = numeros.missing_num(n, list1, m, list2)
print('The missing numbers in list 1 is:', missing_numbers)