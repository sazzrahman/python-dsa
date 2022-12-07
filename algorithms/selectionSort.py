import unittest

# compares each item to the elements to left of it


def find_min_index(arr: list) -> int:
    """
    returns the index of the minimum value in given array
    """
    l = len(arr)
    i = 1
    min_index = 0
    while i < l:
        if arr[i] < arr[min_index]:
            min_index = i
        i += 1
    return min_index


def selection_sort(arr: list, i: int) -> list:
    sorted = arr[0:i]
    unsorted = arr[i:]

    # recursion end case: when the index is the len of array
    if i == len(arr):
        return sorted

    else:
        min_idx = find_min_index(unsorted)
        current_min = unsorted.pop(min_idx)
        sorted.append(current_min)
        i += 1
        return selection_sort(sorted+unsorted, i)


class TestSelection(unittest.TestCase):
    def test_selection_sort(self):
        arr = [23, 6, 9, 10, 19, 0, 20]
        sorted = selection_sort(arr, 0)
        resultsorted = [0, 6, 9, 10, 19, 20, 23]
        print(sorted)
        self.assertEqual(sorted, resultsorted)

    def test_min_index(self):
        arr = [23, 6, 9, 10, 19, 0, 20]
        idx = find_min_index(arr)
        self.assertEqual(idx, 5)


if __name__ == "__main__":
    unittest.main()
