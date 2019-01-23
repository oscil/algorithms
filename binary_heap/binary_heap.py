#for visualization use http://btv.melezinek.cz/binary-heap.html

import random
import copy
import math


class BinaryHeap:

    """Universal binary heap.
    Default comparison function is for MAX binary heap of numbers of smth with determined __lt__(a,b) operator. """

    def __init__(self, compare=lambda x, y: x < y):
        self.array = []
        self._compare = compare

    def add(self, val):
        self.array.append(val)
        self._up(len(self.array) - 1)

    def get_root(self):
        self._swap(0, len(self.array) - 1)
        out = self.array.pop()
        if len(self.array) > 1:
            self._down(0)
        return out

    def from_list(self, input_list):
        self.array = []
        for value in input_list:
            self.add(value)

    def get_sorted(self):
        """"This func destroys binary heap array, but returns a sorted data. ascent for MIN heap, and descent for MAX heap.
        If you need descent sort MIN heap (or ascent sort for MAX heap)- you have to rebuild the heap- create new heap with other comparison function.
        This sort function is slower than Python's default function sorted() in about 100 times, but it works :)
        """
        out = []
        while len(self.array):
            out.append(self.get_root())
        return out

    def _parent(self, index):
        return self.array[math.floor((index - 1) / 2)], math.floor((index - 1) / 2)

    def _l_child(self, index):
        out_index = (index + 1)*2 - 1
        if out_index < len(self.array):
            return self.array[out_index], out_index
        else:
            return self.array[index], index

    def _r_child(self, index):
        out_index = (index + 1)*2
        if out_index < len(self.array):
            return self.array[out_index], out_index
        else:
            return self.array[index], index

    def _swap(self, index1, index2):
        self.array[index1], self.array[index2] = self.array[index2], self.array[index1]

    def _up(self, index):
        parent_value, parent_index = self._parent(index)
        while self._compare(self.array[index], parent_value) and index > 0:
            self._swap(index, parent_index)
            index = parent_index
            parent_value, parent_index = self._parent(index)

    def _down(self, index):
        while True:
            child_l_val, child_l_index = self._l_child(index)
            child_r_val, child_r_index = self._r_child(index)
            child_val, child_index = (child_r_val, child_r_index) \
                                                   if self._compare(child_r_val, child_l_val) \
                                                   else (child_l_val, child_l_index)

            if self._compare(child_val, self.array[index]):
                self._swap(index, child_index)
                index = child_index
            else:
                return


class MaxBinaryHeap(BinaryHeap):
    def __init__(self):
        super().__init__(compare=lambda x, y: x > y)


class MinBinaryHeap(BinaryHeap):
    def __init__(self):
        super().__init__(compare=lambda x, y: x < y)


if __name__ == '__main__':
    #Create input data
    array_size = 200000
    input_array = []
    for i in range(array_size):
        input_array.append(random.randint(0, 100000))
    random.shuffle(input_array)
    print("Input array = " + str(input_array))

    def check_max_binary_heap(input_data):
        bh = MaxBinaryHeap()
        for v in input_data:
            bh.add(v)
        print("Array in MAX binary heap: " + str(bh.array))

        while len(bh.array):
            prev_bh_array = copy.copy(bh.array)
            m1 = max(bh.array)
            m2 = bh.get_root()
            # check that got MAXIMUM is correct
            if m1 != m2:
                print("ERROR!!!! m1 = " + str(m1) + " m2 = " + str(m2))
                print("arr was: ")
                print(prev_bh_array)
                break


    def check_min_binary_heap(input_data):
        bh = MinBinaryHeap()
        for v in input_data:
            bh.add(v)
        print("Array in MIN binary heap: " + str(bh.array))

        while len(bh.array):
            prev_bh_array = copy.copy(bh.array)
            m1 = min(bh.array)
            m2 = bh.get_root()
            # check that got MINIMUM is correct
            if m1 != m2:
                print("ERROR!!!! m1 = " + str(m1) + " m2 = " + str(m2))
                print("arr was: ")
                print(prev_bh_array)
                break

    def check_sorted(input_data):
        bh = MinBinaryHeap()
        for v in input_data:
            bh.add(v)
        print("Array in MIN binary heap for sort: " + str(bh.array))

        while len(bh.array):
            m1 = sorted(bh.array)
            m2 = bh.get_sorted()
            # check that sort is correct is correct
            for i in range(len(m1)):
                if m1[i] != m2[i]:
                    print("ERROR m1[{}] != m2[{}]".format(i,i))
                    break


    check_max_binary_heap(input_array)
    check_min_binary_heap(input_array)
    check_sorted(input_array)












