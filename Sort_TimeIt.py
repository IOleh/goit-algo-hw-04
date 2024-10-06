import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація випадкового масиву
arr = [random.randint(1, 10000) for _ in range(1000)]

# Заміри часу для сортування злиттям
time_merge_sort = timeit.timeit(lambda: merge_sort(arr.copy()), number=100)
# Заміри часу для сортування вставками
time_insertion_sort = timeit.timeit(lambda: insertion_sort(arr.copy()), number=100)
# Заміри часу для вбудованого Timsort
time_tim_sort = timeit.timeit(lambda: sorted(arr.copy()), number=100)

print(f"Merge Sort: {time_merge_sort} seconds")
print(f"Insertion Sort: {time_insertion_sort} seconds")
print(f"Timsort (built-in): {time_tim_sort} seconds")
