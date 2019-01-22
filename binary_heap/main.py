#for visualization use http://btv.melezinek.cz/binary-heap.html

import random
import copy
import math


class BinaryHeap:
    """Max binary heap"""

    def __init__(self):
        self.array = []

    def add(self, val):
        self.array.append(val)
        self._up(len(self.array) - 1)

    def get_max(self):
        self._swap(0, len(self.array) - 1)
        out = self.array.pop()
        if len(self.array) > 1:
            self._down(0)
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
        while parent_value < self.array[index] and index > 0:
            self._swap(index, parent_index)
            index = parent_index
            parent_value, parent_index = self._parent(index)

    def _down(self, index):
        while True:
            child_l_val, child_l_index = self._l_child(index)
            child_r_val, child_r_index = self._r_child(index)
            child_val, child_index = (child_r_val, child_r_index) \
                                                   if child_r_val > child_l_val \
                                                   else (child_l_val, child_l_index)

            if self.array[index] < child_val:
                self._swap(index, child_index)
                index = child_index
            else:
                return


if __name__ == '__main__':
    array_size = 200
    input_array = []
    for i in range(array_size):
        input_array.append(random.randint(0, 100))
    random.shuffle(input_array)

    bh = BinaryHeap()

    print("Input array = " + str(input_array))
    for v in input_array:
        bh.add(v)
    print("Array in binary heap= " + str(bh.array))

    while len(bh.array):
        prev_bh_array = copy.copy(bh.array)
        m1 = max(bh.array)
        m2 = bh.get_max()
        # check that got MAXIMUM is correct
        if m1 != m2:
            print("ERROR!!!! m1 = " + str(m1) + " m2 = " + str(m2))
            print("arr was: ")
            print(prev_bh_array)
            break



