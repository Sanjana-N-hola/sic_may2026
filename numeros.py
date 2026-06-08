def missing_num(n, list1, m, list2):
    missing_num_list=[]

    for i in set(list2):
        if list2.count(i) != list1.count(i):
            for j in range(list2.count(i)-list1.count(i)):
                missing_num_list.append(i)

    return sorted(missing_num_list)