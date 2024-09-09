"""
 [*] Bubble Sort Algorithm:
    Write a program to sort a list of numbers using the bubble sort algorithm with nested for loops.

"""

list_rang= int(input(" Enter the list rang number : "))
values_list = []

for i in range(list_rang):
    value = input("Enter the value: ")
    values_list.append(int(value))
def bubble_sort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
    return list_a
print(f"Sorted list: {bubble_sort(values_list)} ")
