def linear_search(searchele,elements):
    for i in range(len(elements)):
        if elements[i] == searchele:
            return i
    return -1
input_size = int(input('Enter size of list'))
elements=[]
print(f'Enter the {input_size} elements of the list')
for i in range(input_size):
    element=float(input())
    elements.append(element)

print('User given elements are\n',elements)
searchele=