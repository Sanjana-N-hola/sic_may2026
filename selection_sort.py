def selection_sort(numbers):
    
    for i in range(len(numbers)):
        min_number = i
        for j in range(i+1, len(numbers)):
            if numbers[min_number] > numbers[j]:
                min_number = j
        if i != min_number:
            numbers[i], numbers[min_number] = numbers[min_number], numbers[i]
    return numbers
            
   
                
                