import unittest

# compares each item to the elements to left of it


def find_index(arr: list, item: int) -> list:
    """
    returns the index where the item should be inserted
    """
    l = len(arr)
    i = l-1
    idx = l-1
    while i >= 0:
        if item <= arr[i]:
            idx = i
        i -= 1
    return idx


def insertion_sort(arr: list, i: int) -> list:
    """
    arr : given unsoerted arry
    l : length of the current arry
    i: index must begin with 1
    """
    sorted = arr[0:i]
    unsorted = arr[i+1:]
    l = len(arr)
    if l == i:
        return arr
    else:
        item = arr[i]
        idx = find_index(sorted, item)
        sorted.insert(idx, item)
        print(sorted)
        i += 1
        return insertion_sort(sorted+unsorted, i)


class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        arr = [23, 6, 9, 10, 19, 0, 20]
        sorted = insertion_sort(arr, 1)
        resultsorted = [0, 6, 9, 10, 19, 20, 23]
        self.assertEqual(sorted, resultsorted)
        print(sorted)

    def test_find_index(self):
        arr = [1, 5, 9, 22]
        item = 7
        result = find_index(arr, item)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
