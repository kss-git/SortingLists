def merge_sorted_lists(list1, list2):
    merged_list = []
    p1 = 0
    p2 = 0

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            merged_list.append(list1[p1])
            p1 += 1
        else:
            merged_list.append(list2[p2])
            p2 += 1

    # Append any remaining elements
    merged_list.extend(list1[p1:])
    merged_list.extend(list2[p2:])

    return merged_list

list_a = [1, 3, 5, 7]
list_b = [2, 4, 6, 8]
result = merge_sorted_lists(list_a, list_b)
print(result)