def divide_array(numbers, low, high):
    if low < high:
	    mid = (low+high) // 2
        divide_array(numbers,  )
	    array_a = numbers[mid+1:]
	    array_b = numbers[low: mid+1]
		merge(array_a, array_b)
		

def merge(array_a, array_b):
	merged_array = []
    i = j = k = 0
    while i < len(array_a) and j < len(array_b):
		if array_a[i] < array_b[j]:
			merged_array[k] = array_a[i]
			i += 1
		else:
			merged_array[k] = array_b[j]
			j += 1
		k += 1
	merged_array[k: ] = array_a[i: ]
	merged_array[k: ] = array_a[j: ]

with open()