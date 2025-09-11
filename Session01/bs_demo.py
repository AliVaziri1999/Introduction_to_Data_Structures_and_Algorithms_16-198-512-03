import time
import matplotlib.pyplot as plt

# ---------- Binary Search with step counter ----------
def binary_search_with_counter(arr, x):
    # steps: count how many times the while loop executes
    steps = 0
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        steps += 1
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return True, steps
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False, steps

# ---------- Binary Search without counter (for timing) ----------
def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

# ---------- Helpers ----------
def make_sorted_array(n):
    # create a sorted array: [0, 1, 2, ..., n-1]
    return list(range(n))

def measure_once(func, arr, x):
    # measure one execution of the function
    t0 = time.perf_counter()
    func(arr, x)
    t1 = time.perf_counter()
    return t1 - t0

def measure_best_of(func, arr, x, repeat=9):
    # run multiple times and take the best (to reduce noise)
    best = float('inf')
    for _ in range(repeat):
        dt = measure_once(func, arr, x)
        if dt < best:
            best = dt
    return best

# ---------- Main ----------
if __name__ == "__main__":
    # Example 1: very small and easy to understand
    arr = [1, 3, 5, 7, 9]          # input must be sorted
    target = 7                      # exists in the array
    found, steps = binary_search_with_counter(arr, target)
    print("Example 1")
    print(f"arr={arr}, target={target} -> found={found}, steps={steps}")

    target = -1                     # does not exist (worst case)
    found, steps = binary_search_with_counter(arr, target)
    print(f"arr={arr}, target={target} -> found={found}, steps={steps}")
    print()

    # Example 2: growth with increasing n
    print("         n        steps     time_ms  time/prev")
    prev_time = None

    sizes = []
    steps_list = []
    times_list = []

    for k in range(10, 21):         # n = 1024 to 1,048,576
        n = 2 ** k
        arr = make_sorted_array(n)
        target = -1                 # deliberately missing (worst case)

        # count steps (log n should grow slowly)
        _, steps = binary_search_with_counter(arr, target)

        # measure real time
        dt_ms = measure_best_of(binary_search, arr, target, repeat=9) * 1e3
        ratio = (dt_ms / prev_time) if prev_time else float('nan')

        print(f"{n:10d} {steps:10d} {dt_ms:12.3f} {ratio:10.2f}")

        # store for plotting
        sizes.append(n)
        steps_list.append(steps)
        times_list.append(dt_ms)

        prev_time = dt_ms

    # ---------- Plotting ----------
    plt.figure(figsize=(10,5))

    # Plot timing
    plt.subplot(1,2,1)
    plt.plot(sizes, times_list, marker='o')
    plt.xscale("log")   # log scale for input size
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (ms)")
    plt.title("Binary Search Runtime")

    # Plot steps
    plt.subplot(1,2,2)
    plt.plot(sizes, steps_list, marker='o', color='red')
    plt.xscale("log")
    plt.xlabel("Input size (n)")
    plt.ylabel("Steps (counter)")
    plt.title("Binary Search Steps")

    plt.tight_layout()
    plt.show()
