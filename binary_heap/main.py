#for visualization use http://btv.melezinek.cz/binary-heap.html

import random
import copy
import math


class BinaryHeap:

    def __init__(self):
        self.arr = []

    def add(self, val):
        self.arr.append(val)
        self._up(len(self.arr)-1)

    def get_max(self):
        self._swap(0, len(self.arr)-1)
        out = self.arr.pop()
        if len(self.arr) > 1:
            self._down(0)
        return out

    def _parent(self, index):
        return self.arr[math.floor((index-1)/2)], math.floor((index-1)/2)

    def _lchild(self, index):
        out_index = (index + 1)*2 - 1
        if out_index < len(self.arr):
            return self.arr[out_index], out_index
        else:
            return self.arr[index], index

    def _rchild(self, index):
        out_index = (index + 1)*2
        if out_index < len(self.arr):
            return self.arr[out_index], out_index
        else:
            return self.arr[index], index

    def _swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]

    def _up(self, index):
        pval, pi = self._parent(index)
        while pval < self.arr[index] and index > 0:
            self._swap(index, pi)
            index = pi
            pval, pi = self._parent(index)

    def _down(self, index):
        while True:
            clval, cli = self._lchild(index)
            crval, cri = self._rchild(index)
            cval, ci = (crval, cri) if crval > clval else (clval, cli)

            if self.arr[index] < cval:
                self._swap(index, ci)
                index = ci
            else:
                return






size = 200

arr = []
for i in range(size):
    arr.append(random.randint(0, 100))
random.shuffle(arr)

bh = BinaryHeap()

print("ARR = " + str(arr))
for v in arr:
    bh.add(v)
print("BH_ARR = " + str(bh.arr))


while len(bh.arr):
    prevarr = copy.copy(bh.arr)
    m1 = max(bh.arr)
    m2 = bh.get_max()
    # print("after = " + str(bh.arr))
    if m1 != m2:
        print("ERROR!!!! m1 = " + str(m1) + " m2 = " + str(m2))
        print("arr was: ")
        print(prevarr)
        break



