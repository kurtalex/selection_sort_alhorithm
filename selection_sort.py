def find_minimal_element(arr):
    minimal_element = arr[0]
    minimal_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < minimal_element:
            minimal_element = arr[i]
            minimal_element_index = i
    return minimal_element_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        minimal_element = find_minimal_element(arr)
        new_arr.append(arr.pop(minimal_element))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
