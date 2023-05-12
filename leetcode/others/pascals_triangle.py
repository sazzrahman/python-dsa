import unittest


def pair_sum(arr: list) -> list:
    window_size = 1
    output = []
    i = 0
    while i < len(arr)-1:
        output.append(arr[i] + arr[i+window_size])
        i += 1
    return output


def get_next_row(arr):
    if len(arr) == 0:
        return [1]
    if len(arr) == 1:
        return [1, 1]
    else:
        current_arr = [1] + pair_sum(arr) + [1]
        return current_arr


def pascal_triangle(numRows: int):
    i = 0
    output = [[]]
    while i < numRows:
        output.append(get_next_row(output[-1]))
        i += 1

    return output[1:]


class TestMethod(unittest.TestCase):
    def test_base(self):

        print(pascal_triangle(5))
        print(pascal_triangle(1))

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
