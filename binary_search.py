import sys

input_numbers = []
print(f'User given elements are')
for i in range(1, len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print(f'User given elements are \n', input_numbers)

search_element