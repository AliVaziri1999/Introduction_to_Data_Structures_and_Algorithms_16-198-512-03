# check_hw8.py
from edit02PriorityQueueHW import StackUsingPriorityQueue, QueueUsingPriorityQueue, findKthElement
import random, heapq

def test_stack():
    s = StackUsingPriorityQueue()
    assert s.is_empty()
    for x in [1, 2, 3]:
        s.push(x)
    assert s.pop() == 3
    assert s.pop() == 2
    s.push(99)
    assert s.pop() == 99
    assert s.pop() == 1
    assert s.is_empty()
    print("Stack tests passed")

def test_queue():
    q = QueueUsingPriorityQueue()
    assert q.is_empty()
    for x in [1, 2, 3]:
        q.enqueue(x)
    assert q.dequeue() == 1
    q.enqueue(99)
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 99
    assert q.is_empty()
    print("Queue tests passed")

def test_kth_examples():
    assert findKthElement([3,2,1,5,9,4], 2) == 5
    assert findKthElement([3,2,3,0,2,4,5,7,6], 4) == 4
    print("findKthElement example tests passed")

def test_kth_random():
    # Compare against a trusted reference: heapq.nlargest (testing only)
    for _ in range(200):
        n = random.randint(1, 60)
        k = random.randint(1, n)
        lst = [random.randint(-1000, 1000) for _ in range(n)]
        expected = heapq.nlargest(k, lst)[-1]
        got = findKthElement(lst, k)
        assert got == expected, f"Mismatch on {lst=} {k=}: {got=} {expected=}"
    print("findKthElement randomized tests passed")

if __name__ == "__main__":
    test_stack()
    test_queue()
    test_kth_examples()
    test_kth_random()
    print("\nAll tests passed ✅")
