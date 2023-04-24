import unittest

# remove all adjacent duplicates in a string


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.length = 0

    def pop(self):
        self.length -= 1
        return self.stack.pop()

    def get(self):
        if self.length == 0:
            return None
        else:
            # Negative index will never used
            return self.stack[self.length-1]

    def push(self, value: int):
        self.stack.append(value)
        self.length += 1


def remove_duplicates(s: str) -> int:
    stack = Stack()
    l = len(s)
    i = 0
    while i < l:
        current_str = s[i]
        previous_str = stack.get()
        if not previous_str:
            stack.push(current_str)
            i += 1
            continue

        if previous_str == current_str:
            stack.pop()
            i += 1
        else:
            stack.push(current_str)
            i += 1

    return stack.stack


class TestMethod(unittest.TestCase):
    def test_base(self):

        base_input = "sadkkdassa"
        short_input = "abbaaca"
        print(remove_duplicates(base_input))
        print(remove_duplicates(short_input))

        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
