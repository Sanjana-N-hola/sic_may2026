def partition_array(numbers, low, high):
    numbers = []
    pivot = numbers[-1]
    i = low
    j = high
    
    for i in range(len(numbers)-1):
        if numbers[i] < pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[-1], numbers[j] = numbers[j], numbers[-1]
    return j

def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partition_array(numbers, low, high)
        print(numbers)
        quick_sort(numbers, low, pivot_index)
        quick_sort(numbers, pivot_index+1, high)