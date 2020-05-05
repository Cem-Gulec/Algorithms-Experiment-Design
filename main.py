import math

class max_heap:

    def __init__(self, items = []):
        super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.heapify_up(len(self.heap)-1)
    
    def push(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
    
    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap)-1)
            max = self.heap.pop()
            self.heapify_down(1)
        
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        
        return max
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index):
        parent = index // 2
        if index <= 1:
            return

        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.heapify_up(parent)
    
    def heapify_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        
        if largest != index:
            self.swap(index, largest)
            self.heapify_down(largest)

def swap_array(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list

def quick_select_ver1(list, k):

    pivot = list[0]
    arr1, arr2 = [], []

    for i in range(1, len(list)):
        if list[i] < pivot:
            arr1.append(list[i])
        elif list[i] > pivot:
            arr2.append(list[i])
        else: pass


    if k <= len(arr1):
        return quick_select_ver1(arr1, k)
    elif k > len(list) - len(arr2):
        return quick_select_ver1(arr2, k-( len(list)-len(arr2) ))
    else:
        return pivot

def quick_select_ver2(list, left, right, k):

    if k > 0 and k <= right-left+1:
        index = partition(list, left, right)

        if index-1 == k-1:
            return list[index]

        if index-1 > k-1:
            return quick_select_ver2(list, 1, index-1, k)

        return quick_select_ver2(list, index+1,
                                 right, k-index+left-1)

def partition(list, left, right):

    pivot = list[right]
    tmp_index = left

    for i in range(left,right):
        if list[i] <= pivot:
            swap_array(list, i, tmp_index)
            tmp_index += 1

    swap_array(list, right, tmp_index)

    return tmp_index

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
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

        i += 1

    return array


if __name__ == "__main__":
    arr = [10, 15, 40, 45, 55, 8, 6, 11, 26, 4 , 44, 41, 42, 56, 57,78,79,80,81,82]

    #-------insertion sort-------#
    insertion_sorted_arr = insertion_sort(arr)
    mid_element_ins = insertion_sorted_arr[math.ceil(len(insertion_sorted_arr)/2)-1]
    print("after having insertion sort: ", insertion_sorted_arr, "\n⌈n/2⌉'th element in the list (median): ", mid_element_ins)

    #-------merge sort-----------#
    merge_sorted_arr = merge_sort(arr)
    mid_element_mrg = merge_sorted_arr[math.ceil(len(merge_sorted_arr) / 2) - 1]
    print("\nafter having merge sort: ", merge_sorted_arr, "\n⌈n/2⌉'th element in the list (median): ", mid_element_mrg)

    #building max heap and returning root after n/2 removals
    heap = max_heap(arr)
    for i in range(math.floor(len(arr)/2)): heap.pop()
    print("\nafter having ⌊n/2⌋ times removal head of heap returned (median of list): ", heap.peek())

    # quick select using first element as pivot
    quick_selected_arr_ver1 = quick_select_ver1(arr, math.ceil(len(arr) / 2))
    print("\nafter implementing quick select ver#1, median: ", quick_selected_arr_ver1)

    quick_selected_arr_ver2 = quick_select_ver2(arr, 0, len(arr)-1, math.ceil(len(arr) / 2)-1)
    print("\nafter implementing quick select ver#2, median: ", quick_selected_arr_ver2)