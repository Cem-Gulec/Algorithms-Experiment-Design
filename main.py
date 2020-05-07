import math
import time
import sys


#global counter variables
counter_is, counter_mrg, counter_heap, counter_qui_ver1, counter_qui_ver2 = 0, 0, 0, 0, 0


class max_heap:

    # constructor
    def __init__(self, items = []):
        super().__init__()
        # creating a list called heap
        self.heap = [0]
        # inserting elements in the list passed as argument
        for i in items:
            # append the item to the heap
            self.heap.append(i)
            # as we append them we need no heapify them up in their correct positions
            self.heapify_up(len(self.heap)-1)

    # checking if we simply have 1 or more value on heap
    # return the head of heap else return false
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        # if there are 2 or more value in the heap
        # swap the max value at the end of the heap before popping
        # then heapify down the value we swapped to the top position
        if len(self.heap) > 2:
            self.swap(1, len(self.heap)-1)  # swap first val <-> last val
            max_element = self.heap.pop()  # pop max val
            self.heapify_down(1)

        # if there is only 1 value on the heap
        # here, we simply can pop the top value and have empty heap
        elif len(self.heap) == 2:
            max_element = self.heap.pop()

        # case where heap is empty
        # which we need to return false
        else:
            max_element = False

        # return resulting value from above cases
        return max_element

    # swap positions in array
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # when we add an element at the end of the heap or list at this representation
    # we need to heapify up it to its correct position
    def heapify_up(self, index):
        # parent index
        parent = index // 2
        # in case it is already at the top
        # simply return without heapifying it up anything
        if index <= 1:
            return

        # if end of the value index is greater than its parent
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)  # swap it with its parent
            self.heapify_up(parent)  # then implement heapify it up to parent node

    # when a node is inserted at the top of the heap
    # heapify it down to its proper position in the heap
    def heapify_down(self, index):

        global counter_heap

        left = index * 2  # index of left
        right = index * 2 + 1  # index of right
        largest = index  # index of the largest value

        # compare our index value to the left child
        # to determine which one is larger
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left

        # compare our index value to the right child
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right

        # if we could not find largest in the position we are searching
        if largest != index:
            self.swap(index, largest)  # swap places
            self.heapify_down(largest)  # and recursively call heapify down on the largest value

        counter_heap += 1


# quick select algorithm where
# we use first item as pivot as the 1st version
# returns: k'th position in a given unsorted array
def quick_select_ver1(array, k):

    global counter_qui_ver1

    pivot = array[0]  # assigning first element as the pivot
    arr1, arr2 = [], []  # empty arrays that will handle the partitioning

    # split our elements as, small elements into -> arr1
    #                        big elements into   -> arr2
    for i in range(1, len(array)):
        # checking if the index is less than the pivot
        if array[i] < pivot:
            arr1.append(array[i])
        # checking if the index is greater than the pivot
        elif array[i] > pivot:
            arr2.append(array[i])
        else: pass

        counter_qui_ver1 += 1

    # if it is in the small element array
    if k <= len(arr1):
        return quick_select_ver1(arr1, k)

    # if it is the big elements array
    elif k > len(array) - len(arr2):
        return quick_select_ver1(arr2, k-( len(array)-len(arr2) ))

    # if it is equal to the pivot
    else:
        return pivot


# returns: k'th position in a given unsorted array
def quick_select_ver2(array, left, right, k):

    sys.setrecursionlimit(10 ** 6)

    # if given k is less than len of array
    if 0 < k <= right-left+1:

        # implement partition
        index = partition(array, left, right)

        # in case of position is the same with given k
        # directly return the index
        if index-1 == k-1:
            return array[index]

        # if position is higher than above condition
        # implement recurrent function to call on left sub-array
        if index-1 > k-1:
            return quick_select_ver2(array, 1, index-1, k)

        # else implement recurrent function to call on right sub-array
        return quick_select_ver2(array, index+1,
                                 right, k-index+left-1)


# moves all smaller element to left of the pivot
# greater elements to right of the pivot
def partition(array, left, right):

    global counter_qui_ver2
    sys.setrecursionlimit(10 ** 6)

    pivot = array[right]  # declaring pivot as the last element
    tmp_index = left  # temporary variable to hold left index, each iteration it will move one by one

    # iterate through left to right
    for i in range(left, right):
        # check whether the index value is less than or equal to pivot
        if array[i] <= pivot:
            array[i], array[tmp_index] = array[tmp_index], array[i]  # if so swap current index and the left index
            tmp_index += 1

        counter_qui_ver2 += 1

    # after all for the final step swap right and the tmp_location
    array[right], array[tmp_index] = array[tmp_index], array[right]

    return tmp_index


def merge_sort(array):

    # simply do not need to execute rest of the lines
    if len(array) <= 1:
        return array

    mid = int(len(array)/2)  # mid-point in the array
    left = merge_sort(array[:mid])  # left-half of the array
    right = merge_sort(array[mid:])  # right-half of the array

    # returning the array which is created
    # after merging left and right half
    return merge(left, right)


def merge(left, right):

    global counter_mrg
    merged = []
    left_pos, right_pos = 0, 0

    # while there exist elements in both left and right half of the array
    while left_pos < len(left) and right_pos < len(right):

        # check which index in the array is lower
        # here, if element in the left array is smaller
        if left[left_pos] < right[right_pos]:
            # append it the array to be returned
            merged.append(left[left_pos])
            left_pos += 1
        # if above is not the case append right
        else:
            merged.append(right[right_pos])
            right_pos += 1

        counter_mrg += 1

    # if the case is that, there are either elements in the left or right
    # simply extend the elements in left and right position all the way to the end
    merged.extend(left[left_pos:])
    merged.extend(right[right_pos:])

    # return resulting array
    return merged


def insertion_sort(array):

    # go until the last element of the array
    global counter_is
    for i in range(1, len(arr)):
        j = i
        # shifting each element one place to the right until
        # a suitable position is found for the new element
        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            counter_is += 1
            j -= 1
        i += 1

    # returning sorted array
    return array


def read_file(arr):
    file1 = open('100k.txt', 'r')
    count = 0

    while True:
        count += 1

        # Get next line from file
        line = file1.readline()

        # end of file
        if not line:
            break
        arr.append(int(line.strip()))

    file1.close()


if __name__ == "__main__":
    # our list four trial
    arr = []
    read_file(arr)

    # -------insertion sort------- #
    t_start_is = time.perf_counter()
    insertion_sorted_arr = insertion_sort(arr)
    t_end_is = time.perf_counter()
    # total time spent in insertion sort
    total_time_is = t_end_is - t_start_is
    # declaring median after implementing sorting
    mid_element_ins = insertion_sorted_arr[math.ceil(len(insertion_sorted_arr)/2)-1]
    print("⌈n/2⌉'th element in the list (median): ", mid_element_ins)
    print("Total time spent in insertion sort is: {:.7f}".format(total_time_is))
    print("Total time the basic operation occurred is: ", counter_is)


    # -------merge sort----------- #
    t_start_mrg = time.perf_counter()
    merge_sorted_arr = merge_sort(arr)
    t_end_mrg = time.perf_counter()
    # total time spent in merge sort
    total_time_mrg = t_end_mrg - t_start_mrg
    # declaring median after implementing sorting
    mid_element_mrg = merge_sorted_arr[math.ceil(len(merge_sorted_arr) / 2) - 1]
    print("\n⌈n/2⌉'th element in the list (median): ", mid_element_mrg)
    print("Total time spent in merge sort is: {:.7f}".format(total_time_mrg))
    print("Total time the basic operation occurred is: ", counter_mrg)


    # building max heap and returning root after n/2 removals
    heap = max_heap(arr)
    t_start_heap = time.perf_counter()
    for i in range(math.floor(len(arr)/2)):
        heap.pop()  # ⌊n/2⌋ times max removal
    t_end_heap = time.perf_counter()
    # total time spent in max heap removal
    total_time_heap = t_end_heap - t_start_heap
    print("\nafter having ⌊n/2⌋ times removal head of heap returned (median of list): ", heap.peek())
    print("Total time spent in max heap removal is: {:.7f}".format(total_time_heap))
    print("Total time the basic operation occurred is: ", counter_heap)


    # quick select using first element as pivot
    t_start_qui_ver1 = time.perf_counter()
    quick_selected_arr_ver1 = quick_select_ver1(arr, math.ceil(len(arr) / 2))
    t_end_qui_ver1 = time.perf_counter()
    # total time spent in quick select ver#1 removal
    total_time_qui_ver1 = t_end_qui_ver1 - t_start_qui_ver1
    print("\nafter implementing quick select ver#1, median: ", quick_selected_arr_ver1)
    print("Total time spent in quick select ver#1 is: {:.7f}".format(total_time_qui_ver1))
    print("Total time the basic operation occurred is: ", counter_qui_ver1)


    # quick select using median-of-three pivot selection
    t_start_qui_ver2 = time.perf_counter()
    quick_selected_arr_ver2 = quick_select_ver2(arr, 0, len(arr)-1, math.ceil(len(arr) / 2)-1)
    t_end_qui_ver2 = time.perf_counter()
    # total time spent in quick select ver#2 removal
    total_time_qui_ver2 = t_end_qui_ver2 - t_start_qui_ver2
    print("\nafter implementing quick select ver#2, median: ", quick_selected_arr_ver2)
    print("Total time spent in quick select ver#1 is: {:.7f}".format(total_time_qui_ver2))
    print("Total time the basic operation occurred is: ", counter_qui_ver2)
