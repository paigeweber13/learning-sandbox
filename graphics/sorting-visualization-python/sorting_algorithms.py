def swap(input_list: [int], index_a: int, index_b: int):
    if index_a == index_b:
        return input_list

    c = input_list[index_a]
    input_list[index_a] = input_list[index_b]
    input_list[index_b] = c
    return input_list

def selection_sort_step(input_list: [int], num_unsorted: int):
    list_len = len(input_list)
    min_index = list_len - num_unsorted - 1
    for i in range(list_len - num_unsorted, list_len):
        if input_list[i] < input_list[min_index]:
            min_index = i
    
    swap(input_list, list_len - num_unsorted - 1, min_index)
    return input_list

def selection_sort(input_list: [int]):
    n = len(input_list)
    for _ in range(len(input_list)):
        selection_sort_step(input_list, n)
        n -= 1
    return input_list
