import unittest


def reverseStringPy(s: str) -> str:
    split_arr = s.split(" ")
    split_arr.reverse()
    return " ".join(split_arr)


def reverseString(s: str) -> str:
    # reverse the string using the slicing method

    reversed = s[::-1]
    start = 0
    end = len(s)-1
    reversed_sentence = ""

    for i in range(len(reversed)):
        if reversed[i] == " " or i == len(reversed)-1:
            end = i+1 if i == len(reversed)-1 else i
            current_word = reversed[start:end][::-1]
            current_word = current_word if i == len(
                reversed)-1 else current_word + " "
            reversed_sentence += current_word
            start = i+1

    return reversed_sentence


class TestReverseString(unittest.TestCase):
    def test_base(self):
        test_input = "Happy Birthday to you !"

        test_output = "! you to Birthday Happy"

        print(reverseString(test_input))
        self.assertEqual(reverseString(test_input), test_output)


if __name__ == "__main__":
    unittest.main()
