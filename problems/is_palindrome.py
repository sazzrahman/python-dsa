import unittest


def is_palindrome(s: str) -> bool:

    # define two pointers
    l = len(s)
    start = 0
    end = l - 1

    while end > start:
        if s[start] == s[end]:
            start += 1
            end -= 1

        else:
            return False
    return True


class TestMethod(unittest.TestCase):
    def test_base(self):

        test_case_1 = "abba"
        test_case_2 = "raceacar"
        test_case_3 = "alicila"

        self.assertTrue(is_palindrome(test_case_1))
        self.assertFalse(is_palindrome(test_case_2))
        self.assertTrue(is_palindrome(test_case_3))


if __name__ == "__main__":
    unittest.main()
