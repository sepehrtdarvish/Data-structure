import math

class Sort():
    def bubble_sort(lst):
        for i in range(len(lst)):
            for j in range(len(lst)-1-i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    def selection_sort(lst):
        sorted_list = []
        for i in range(len(lst)):
            min_num = min(lst)
            sorted_list.append(min_num)
            lst.pop(lst.index(min_num))
        return sorted_list

    def insertion_sort(lst):
        for i in range(1, len(lst)):
            k = i
            for _ in range(i):
                if lst[k] < lst[k-1]:
                    lst[k], lst[k-1] = lst[k-1], lst[k]
                    k -= 1
                else:
                    break
        return lst
    
    def quick_sort(lst):
        if len(lst) <= 1:  # اگر طول لیست یک یا کمتر باشد، لیست مرتب است.
            return lst
        
        pivot = lst[len(lst) // 2]  # انتخاب محور (pivot) از وسط لیست
        left = [x for x in lst if x < pivot]  # عناصر کوچکتر از pivot
        middle = [x for x in lst if x == pivot]  # عناصر برابر با pivot
        right = [x for x in lst if x > pivot]  # عناصر بزرگتر از pivot
        
        # فراخوانی بازگشتی روی لیست‌های چپ و راست
        return Sort.quick_sort(left) + middle + Sort.quick_sort(right)



    def merge_sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = Sort.merge_sort(lst[:mid])
        right = Sort.merge_sort(lst[mid:])

        return Sort.merge(left, right)

    def merge(left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    def count_sort_1(lst):
        output_list = []
        count = [0] * (max(lst) + 1)

        for num in lst:
            count[num] += 1
        
        for i in range(len(count)):
            for j in range(count[i]):
                output_list.append(i)
        return output_list

    def countingSort(arr, exp1):

        n = len(arr)
        output = [0] * (n)

        # initialize count array as 0
        count = [0] * (10)

        # Store count of occurrences in count[]
        for i in range(0, n):
            index = arr[i] // exp1
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp1
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

    # Method to do Radix Sort


    def radixSort(arr):

        # Find the maximum number to know number of digits
        max1 = max(arr)

        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exp = 1
        while max1 / exp >= 1:
            Sort.countingSort(arr, exp)
            exp *= 10

lst = [11,22,83,21,93,81,8,4,911,52]

Sort.radixSort(lst)

print(lst)