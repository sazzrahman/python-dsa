import unittest

# sliding window technique
# given a string and a window size k
# find the substrings that appear more than once


def find_substring(s: str, k: int) -> int:
    # window is mutable list
    window = [0, k]
    substr = {}
    while window[1] <= len(s):

        current_substr = s[window[0]:window[1]]
        if current_substr in substr:
            substr[current_substr] += 1
        else:
            substr[current_substr] = 0

        window[0] += 1
        window[1] += 1

    return substr


class TestMethod(unittest.TestCase):
    def test_base(self):

        base_s = "AGAGCTCCAGAGCTTG"
        base_k = 6

        print(find_substring(base_s, base_k))

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
