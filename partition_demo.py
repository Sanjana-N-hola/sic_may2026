import partition as pt
import sys

numbers = [int(value) for value in sys.argv[1:]]

print('Numbers before partitioning: \n', numbers)
pt.partition_array(numbers)
print('Numbers after partitioning:\n', numbers)
