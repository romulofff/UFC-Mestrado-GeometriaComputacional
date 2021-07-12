from time import time

import numpy as np

#############################################
# ORDENAÇÃO DOS VETORES CRIADOS PELO PYTHON #
#############################################

print("""\n#############################################
# ORDENAÇÃO DOS VETORES CRIADOS PELO PYTHON #
#############################################""")

np.random.seed(42)
n10 = np.random.randint(10, size=10)
n100 = np.random.randint(100, size=100)
n1000 = np.random.randint(1000, size=1000)
nSorted = [i for i in range(10)]

# Python's ordering function
initial_time = time()
sortedN10 = sorted(n10.copy())
sortedN10_time = time() - initial_time
initial_time = time()
sortedN100 = sorted(n100.copy())
sortedN100_time = time() - initial_time
initial_time = time()
sortedN1000 = sorted(n1000.copy())
sortedN1000_time = time() - initial_time
initial_time = time()
sortedNsorted = sorted(nSorted.copy())
sortedNsorted_time = time() - initial_time

print("\nPython's default sorting function uses Timsort algorithm. Here's the time it took to sort each of our arrays.")
print("N = 10 - Elapsed time: ", sortedN10_time, "seconds.")
print("N = 100 - Elapsed time: ", sortedN100_time, "seconds.")
print("N = 1000 - Elapsed time: ", sortedN1000_time, "seconds.")
print("N = 10 sorted - Elapsed time: ", sortedNsorted_time, "seconds.")


######################################
# QUESTÃO 02 - ORDENAÇÃO POR SELEÇÃO #
######################################

print("""\n######################################
# QUESTÃO 02 - ORDENAÇÃO POR SELEÇÃO #
######################################""")


def swap(x, i, m):
    x[i], x[m] = x[m], x[i]
    return x


def selection(x, n):
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if x[j] < x[m]:
                m = j
        x = swap(x, i, m)
    return x


# My ordering function
initial_time = time()
selectedN10 = selection(n10.copy(), len(n10))
selectedN10_time = time() - initial_time
initial_time = time()
selectedN100 = selection(n100.copy(), len(n100))
selectedN100_time = time() - initial_time
initial_time = time()
selectedN1000 = selection(n1000.copy(), len(n1000))
selectedN1000_time = time() - initial_time
initial_time = time()
selectedNSorted = selection(nSorted.copy(), len(nSorted))
selectedNSorted_time = time() - initial_time

# Check if it's the same result
print("\nRunning Selection Sort for all input cases. \nResult \"True\" means our function sorted equally to Python's sorting function.")
print("N = 10 result:", np.array_equal(selectedN10, sortedN10),
      "Elapsed time: ", selectedN10_time, "seconds.")
print("N = 100 result:", np.array_equal(selectedN100, sortedN100),
      "Elapsed time: ", selectedN100_time, "seconds.")
print("N = 1000 result:", np.array_equal(selectedN1000, sortedN1000),
      "Elapsed time: ", selectedN1000_time, "seconds.")
print("N = 10, sorted result:", np.array_equal(selectedNSorted, nSorted),
      "Elapsed time: ", selectedNSorted_time, "seconds.")


########################################
# QUESTÃO 03 - ORDENAÇÃO POR QUICKSORT #
########################################

print("""\n########################################
# QUESTÃO 03 - ORDENAÇÃO POR QUICKSORT #
########################################""")


def divide(p, r, x):
    pivo = x[r]
    i = p-1
    j = p
    while j < r:
        if x[j] <= pivo:
            i += 1
            x = swap(x, i, j)
        j += 1
    x = swap(x, i+1, r)
    return i+1


def quicksort(p, r, x):
    if p >= r:
        return x
    q = divide(p, r, x)
    quicksort(p, q-1, x)
    quicksort(q+1, r, x)
    return x


# My ordering function
initial_time = time()
quickSortN10 = quicksort(0, len(n10)-1, n10.copy())
quickSortN10_time = time() - initial_time
initial_time = time()
quickSortN100 = quicksort(0, len(n100)-1, n100.copy())
quickSortN100_time = time() - initial_time
initial_time = time()
quickSortN1000 = quicksort(0, len(n1000)-1, n1000.copy())
quickSortN1000_time = time() - initial_time
initial_time = time()
quickSortNSorted = quicksort(0, len(nSorted)-1, nSorted.copy())
quickSortNSorted_time = time() - initial_time

# Check if it's the same result
print("\nRunning Quicksort for all input cases. \nResult \"True\" means our function sorted equally to Python's sorting function.")
print("N = 10 result:", np.array_equal(quickSortN10, sortedN10),
      "Elapsed time: ", quickSortN10_time, "seconds.")
print("N = 100 result:", np.array_equal(quickSortN100, sortedN100),
      "Elapsed time: ", quickSortN100_time, "seconds.")
print("N = 1000 result:", np.array_equal(quickSortN1000, sortedN1000),
      "Elapsed time: ", quickSortN1000_time, "seconds.")
print("N = 10, sorted result:", np.array_equal(quickSortNSorted, nSorted),
      "Elapsed time: ", quickSortNSorted_time, "seconds.")


########################################
# QUESTÃO 04 - ORDENAÇÃO POR MERGESORT #
########################################

print("""\n########################################
# QUESTÃO 04 - ORDENAÇÃO POR MERGESORT #
########################################""")


def Merge(l, r, x):
    l = np.append(l, np.inf)
    r = np.append(r, np.inf)
    i = 0
    j = 0
    for k in range(len(x)):
        if l[i] < r[j]:
            x[k] = l[i]
            i += 1
        else:
            x[k] = r[j]
            j += 1
    return x


def MergeSort(x):
    n = len(x)
    if n > 1:
        m = int(n/2)
        l = x[:m]
        r = x[m:]
        # print(l, r)

        MergeSort(l)
        MergeSort(r)
        x = Merge(l, r, x)
        return x


# My ordering function
initial_time = time()
MergeSortN10 = MergeSort(n10.copy())
MergeSortN10_time = time() - initial_time
initial_time = time()
MergeSortN100 = MergeSort(n100.copy())
MergeSortN100_time = time() - initial_time
initial_time = time()
MergeSortN1000 = MergeSort(n1000.copy())
MergeSortN1000_time = time() - initial_time
initial_time = time()
MergeSortNSorted = MergeSort(nSorted.copy())
MergeSortNSorted_time = time() - initial_time


# Check if it's the same result
print("\nRunning MergeSort for all input cases. \nResult \"True\" means our function sorted equally to Python's sorting function.")
print("N = 10 result:", np.array_equal(MergeSortN10, sortedN10),
      "Elapsed time: ", MergeSortN10_time, "seconds.")
print("N = 100 result:", np.array_equal(MergeSortN100, sortedN100),
      "Elapsed time: ", MergeSortN100_time, "seconds.")
print("N = 1000 result:", np.array_equal(MergeSortN1000, sortedN1000),
      "Elapsed time: ", MergeSortN1000_time, "seconds.")
print("N = 10, sorted result:", np.array_equal(MergeSortNSorted, nSorted),
      "Elapsed time: ", MergeSortNSorted_time, "seconds.")


################################
# QUESTÃO 06 - LINHA POLIGONAL #
################################

print("""\n################################
# QUESTÃO 06 - LINHA POLIGONAL #
################################""")

np.random.seed(21)
l10 = np.random.randint(0, 2000, size=([10, 2]))
l100 = np.random.randint(0, 20000, size=([100, 2]))
l1000 = np.random.randint(0, 200000, size=([1000, 2]))


def extrair_i2(a):
    i2 = []
    for i in range(len(a)):
        i2.append(a[i][0])
    return np.array(i2)


def ordena1por2(i1, i2):
    indexes = np.argsort(i2)
    i1 = i1[indexes]

    return i1


def calc_i1(i1, i2):
    i1 = ordena1por2(i1, i2)
    return i1


i2 = extrair_i2(l10.copy())
sortedI10 = calc_i1(l10.copy(), i2)
sortedL10 = np.array(sorted(l10.copy(), key=lambda a: a[0])).tolist()
i2 = extrair_i2(l100.copy())
sortedI100 = calc_i1(l100.copy(), i2)
sortedL100 = np.array(sorted(l100.copy(), key=lambda a: a[0])).tolist()
i2 = extrair_i2(l1000.copy())
sortedI1000 = calc_i1(l1000.copy(), i2)
sortedL1000 = np.array(sorted(l1000.copy(), key=lambda a: a[0])).tolist()

# Check if it's the same result
print("\nRunning MergeSort for all input cases. \nResult \"True\" means our function sorted equally to Python's sorting function.")
print("N = 10 result:", np.array_equal(sortedI10.tolist(), sortedL10))
print("N = 100 result:", np.array_equal(sortedI100.tolist(), sortedL100))
print("N = 1000 result:", np.array_equal(sortedI1000.tolist(), sortedL1000))
print("\n")
