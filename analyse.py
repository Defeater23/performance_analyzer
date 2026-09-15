"""
Algorithm Performance Comparator

Compares performance of Bubble Sort, Insertion Sort, and Merge Sort
using execution time for varying input sizes.
"""

import random
import time
import matplotlib.pyplot as plt


# SORTING ALGORITHMS #

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# PERFORMANCE TEST #

def measure_time(sort_func, arr):

    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()

    return end - start


def main():

    sizes = [100, 500, 1000, 2000]

    bubble_times = []
    insertion_times = []
    merge_times = []

    print("\nAlgorithm Performance Comparison\n")
    print("{:<10} {:<15} {:<15} {:<15}".format(
        "Size", "Bubble", "Insertion", "Merge"))

    for size in sizes:

        data = [random.randint(1, 10000) for _ in range(size)]

        t1 = measure_time(bubble_sort, data)
        t2 = measure_time(insertion_sort, data)
        t3 = measure_time(merge_sort, data)

        bubble_times.append(t1)
        insertion_times.append(t2)
        merge_times.append(t3)

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(
            size, t1, t2, t3))


    # Plot  #

    plt.plot(sizes, bubble_times, marker='o')
    plt.plot(sizes, insertion_times, marker='o')
    plt.plot(sizes, merge_times, marker='o')

    plt.title("Sorting Algorithm Performance Comparison")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")

    plt.legend(["Bubble Sort", "Insertion Sort", "Merge Sort"])

    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()
