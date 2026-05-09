def bubble_sort(elements, len_elements):
    for i in range(0, len_elements-1):
        for j in range(0, len_elements-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    return elements

    
def optimized_bubble_sort(elements, len_elements):
    for i in range(0, len_elements-1):
        sorted = True
        for j in range(0, len_elements-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                sorted = False
        if sorted:
            break 

    return elements
    
    


