import sys
import selection_sort as ss

numbers = []

for i in range(1,len(sys.argv)):
    element = int(sys.argv[i])
    numbers.append(element)

print('Input list for selection sort:', numbers)


print('After selection sort:',ss.selection_sort(numbers))