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
    
    heap = max_heap(arr)
    for i in range(math.floor(len(sorted_arr)/2)): heap.pop()
    print(heap.peek())