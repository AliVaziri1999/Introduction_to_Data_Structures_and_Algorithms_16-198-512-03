"""
Author: Ali Vaziri
Homework 9
Class: DSA 16-198-512-03
Fall 2025
"""

##### Q1
"""
Count pairs (i, j) with i<j and a[i] > a[j].

Approach:
Divide and conquer (merge-sort style).
In merge, when right[j] < left[i], add (mid - i) to the answer.

Time:  O(n log n)
Space: O(n) for the merge buffer.
"""
from typing import List

def count_number_of_transpositions(a: List[int]) -> int:

    if not a:
        return 0

    work = a[:] # working buffer

    def _sort_count(lo: int, hi: int) -> int:
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        inv = _sort_count(lo, mid) + _sort_count(mid, hi)

        i, j = lo, mid
        tmp = []
        while i < mid and j < hi:
            if work[i] <= work[j]:
                tmp.append(work[i]); i += 1
            else:
                inv += (mid - i) # all remaining left elements invert with work[j]
                tmp.append(work[j]); j += 1
        if i < mid: tmp.extend(work[i:mid])
        if j < hi:  tmp.extend(work[j:hi])
        work[lo:hi] = tmp
        return inv

    return _sort_count(0, len(work))



#### Test Q1:
print("\nTest Q1:")
for arr in ([8,4,2,1], [1,2,3,4], [3,1,2], [2,1,3,1,2]):
    print(f"{arr} -> {count_number_of_transpositions(arr)}")
'''
Test Q1:
[8, 4, 2, 1] -> 6
[1, 2, 3, 4] -> 0
[3, 1, 2] -> 2
[2, 1, 3, 1, 2] -> 4
'''


##### Q2
"""
Print all (a[i], a[j]) with i<j and a[i] > a[j].

Approach:
Standard divide-and-conquer (merge-sort over (value, index)). During the merge, whenever right[j] < left[i],
every remaining left[ii] (i ≤ ii < mid) forms a transposition with right[j]; emit those pairs.

Time:  O(n log n + k) where k is the number of printed pairs.
Space: O(n)
"""

from typing import List, Tuple

def print_transpositions(S: List[int]) -> List[Tuple[int, int]]:

    if not S:
        print("No transpositions found")
        return []

    arr = [(S[i], i) for i in range(len(S))]
    buf = arr[:]
    out_pairs: List[Tuple[int, int]] = []

    def _sort_emit(lo: int, hi: int):
        if hi - lo <= 1: return
        mid = (lo + hi) // 2
        _sort_emit(lo, mid)
        _sort_emit(mid, hi)

        i, j = lo, mid
        tmp = []
        while i < mid and j < hi:
            if buf[i][0] <= buf[j][0]:
                tmp.append(buf[i]); i += 1
            else:
                # buf[i].val > buf[j].val  -->  every remaining left[ii] is a transposition with right[j]
                val_r = buf[j][0]
                for ii in range(i, mid):
                    out_pairs.append((buf[ii][0], val_r))
                tmp.append(buf[j]); j += 1

        if i < mid: tmp.extend(buf[i:mid])
        if j < hi:  tmp.extend(buf[j:hi])
        buf[lo:hi] = tmp

    _sort_emit(0, len(buf))


    if out_pairs:
        print("Transpositions (left > right):")
        for p in out_pairs:
            print(p)
    else:
        print("No transpositions found")
    return out_pairs



#### Test Q2:
print("\nTest Q2:")
for S in ([8,4,2,1], [1,2,3,4], [3,1,2], [2,1,3,1,2]):
    print(f"Input: {S}")
    pairs = print_transpositions(S) # prints all
    print(f"k = {len(pairs)}\n")
'''
Test Q2:
Input: [8, 4, 2, 1]
Transpositions (left > right):
(8, 4)
(2, 1)
(4, 1)
(8, 1)
(4, 2)
(8, 2)
k = 6

Input: [1, 2, 3, 4]
No transpositions found
k = 0

Input: [3, 1, 2]
Transpositions (left > right):
(3, 1)
(3, 2)
k = 2

Input: [2, 1, 3, 1, 2]
Transpositions (left > right):
(2, 1)
(3, 1)
(3, 2)
(2, 1)
k = 4
'''


##### Q3
"""
Approach:
Keep doing full passes around the circle;
compare first() vs second() - swap if needed - then move_first_to_bottom()
Repeat passes until a full pass makes no swaps.

Time (worst-case): O(n^2)
space: O(1)
"""
from random import shuffle

class Sort:
    def __init__(self, N):
        self._list = [x for x in range(N)]
        shuffle(self._list)

    def first(self):
        return self._list[0]

    def second(self):
        return self._list[1]

    def swap_top_two(self):
        self._list[0], self._list[1] = self._list[1], self._list[0]

    def move_first_to_bottom(self):
        first = self._list.pop(0)
        self._list.append(first)

    def size(self):
        return len(self._list)

    def sort(self):

        n = self.size()
        if n <= 1:
            return

        for m in range(n, 1, -1): # m = size of the prefix we are bubbling through

            for _ in range(m - 1): # (m-1) compare/swap/rotate steps over the active prefix
                if self.first() > self.second():
                    self.swap_top_two()
                self.move_first_to_bottom()

            # rotate the rest so the head returns to the same spot
            # this keeps the newly placed maximum at the very end (tail)
            for _ in range(n - (m - 1)):
                self.move_first_to_bottom()

    def is_sorted(self):
        for i in range(self.size()-1):
            if self._list[i] > self._list[i+1]:
                return False
        return True

    def __repr__(self):
        return str(self._list)

if __name__ == "__main__":
    c = Sort(20)
    print("BEFORE:", c)
    c.sort()
    print("AFTER :", c)
    print(c.is_sorted())



'''
Q3 output:

BEFORE: [15, 12, 1, 16, 13, 11, 7, 0, 18, 5, 17, 3, 8, 14, 9, 6, 2, 4, 19, 10]
AFTER : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
True
'''