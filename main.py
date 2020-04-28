import math

def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid = int(len(array)/2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)

    
def merge(left, right):
    
    result = []
    left_point = right_point = 0

    while left_point < len(left) and right_point < len(right):

        if left[left_point] < right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1

    result.extend(left[left_point:])
    result.extend(right[right_point:])

    return result

def insertion_sort(array): 
  
    for i in range(1, len(arr)): 
        key = array[i] 
   
        j = i-1
        while j >=0 and key < array[j]: 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = key 

    return array


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6] 
    sorted_arr = insertion_sort(arr)
    middle_element = sorted_arr[math.ceil(len(sorted_arr)/2)-1]
    
    print(sorted_arr, middle_element)
