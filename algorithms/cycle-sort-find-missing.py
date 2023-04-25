import unittest

# Given a list of numbers, sort them in ascending order using cycle sort.
# problem 1: find the missing number in a list of numbers in range of 1 to n


def cycle_sort(nums, pos, counter):

    l = len(nums)
    if counter == 12:
        return nums
    if pos >= l:
        for i in range(l):
            if i+1 != nums[i]:
                return i+1
    current_element = nums[pos]

    if current_element == pos+1 or current_element > l:
        # correct place
        print(pos, nums)
        return cycle_sort(nums, pos+1, counter+1)

    else:
        # switch with the appropriate index
        prev_num = nums[current_element-1]
        nums[current_element-1] = current_element
        nums[pos] = prev_num
        print(pos, nums)
        return cycle_sort(nums, pos, counter+1)


class TestMethod(unittest.TestCase):
    def test_base(self):

        base_input = [5, 2, 3, 1, 8, 7, 4]
        base_output = 6

        self.assertEqual(cycle_sort(base_input, 0, 0), base_output)


if __name__ == "__main__":
    unittest.main()
