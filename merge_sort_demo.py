import sys
import merge_sort as ms

ori_array=[int(i) for i in sys.argv[1:]]

print('Array before sorting using merge sort:',ori_array)

ms.divide_array(ori_array, 0, len(ori_array)-1)

print('Array after sorting using merge sort:',ori_array)