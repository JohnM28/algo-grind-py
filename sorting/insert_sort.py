"""
insert sort is a simple sorting algorithm that builds the final sorted array one item at a time.
by comparing each item with the previous items and swapping them if they are in the wrong order.
"""


def insert_sort_v2(arr: list) -> list:
    """
    more concise version
    """
    for i in range(1, len(arr)):
        j = i - 1
        value = arr[i]
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr


def insert_sort(arr: list) -> list:
    """
    insert sort
    """
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0:
            value = arr[j + 1]
            if arr[j] > value:
                arr[j + 1] = arr[j]
                arr[j] = value
            j -= 1
    return arr


if __name__ == '__main__':
    arr = [5, 3, 2, 4, 1]
    print(insert_sort(arr))
    print(insert_sort_v2(arr))
    arr = [5, 3, 10, 4, 1, 6, 2]
    print(insert_sort(arr))
    print(insert_sort_v2(arr))
