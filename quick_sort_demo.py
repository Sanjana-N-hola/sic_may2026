import quick_sort as qs
import sys

numbers = [int(value) for value in sys.argv[1:]]

print('Numbers before partitioning: \n', numbers)
qs.quick_sort(numbers, 0, len(numbers)-1)
print('Numbers after partitioning:\n', numbers)



