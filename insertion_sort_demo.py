import sys
import insertion_sort as Is

numbers = []
for i in range(1, len(sys.argv)):
    element = sys.argv[i]
    numbers.append(element)

print('The received input is:', numbers)

Is.insertion_sort(numbers)

print('After sorting', numbers)
