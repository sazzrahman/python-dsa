import unittest


def binarySearch(arr: list, target: int, l: int, h: int) -> list:
    """
    recursively finds the target item in a sorted array.
    to return an index we cannot break the array, we pass the full array with corresponding pointers.
    m: the current midpoint of the array
    l: low pointer
    h: high pointer
    
    we need low and high to indicate end of traversal.
    input array must be sorted in ascending order
    """

    if l>h:
        return -1
    
    m = (l+h)//2

    if target == arr[m]:
        return m

    elif target > arr[m]:
        # change m
        l = m+1
        return binarySearch(arr, target, l,h)
    else:
        h = m
        return binarySearch(arr, target, l,h)


class TestMethod(unittest.TestCase):
    def test_base(self):

        test_input = [3, 7, 9, 11, 15, 17, 18, 20, 25, 27, 29, 30, 33, 37]
        test_target = 37
        test_output = 13
        test_len = len(test_input)
        self.assertEqual(binarySearch(test_input, test_target, 0, test_len-1),test_output)


if __name__ == "__main__":
    unittest.main()

# reformat : SHIFT + OPTION + F
