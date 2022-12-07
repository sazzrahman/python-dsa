import argparse

# bubble sort using recursion and while loop
# average time complexity O(N2)
# works well when array is partially sorted


def bubble_sort(arr: list, l: int) -> list:
    """
    arr : a list of unsorted numbers
    returns a sorted list
    """
    if l == 1:
        return arr
    i = 0
    while i < l-1:

        if arr[i] > arr[i+1]:
            # store the values before swapping
            a, b = arr[i], arr[i+1]
            arr[i] = b
            arr[i+1] = a
            i += 1
        else:
            i += 1
    return bubble_sort(arr, l-1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--arr", nargs="+", type=float)
    args = parser.parse_args()
    l = len(args.arr)
    print(bubble_sort(args.arr, l))
