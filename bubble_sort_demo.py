import sys
import bubble_sort as bs

elements=[]

for i in range(1, len(sys.argv)):
    elements.append(float(sys.argv[i]))

len_elements=len(elements)

print(f'User given elements to be sorted are \n', elements)

print('Sorted list with bubble sort:', bs.bubble_sort(elements, len_elements))

print('Sorted list with optimised bubble sort:', bs.bubble_sort(elements, len_elements))


