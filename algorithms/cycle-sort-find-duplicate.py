import unittest

# Given a list of numbers, sort them in ascending order using cycle sort.
# problem 1: find the duplicate number in a list of numbers in range of 1 to n


def cycle_sort(nums, pos, counter):

    l = len(nums)
    if counter == 12:
        return nums
    if pos >= l:
        for i in range(l):
            if i+1 != nums[i]:
                return i+1
    current_element = nums[pos]

    if current_element == pos+1:
        # current element is in correct
        print(pos, nums)
        return cycle_sort(nums, pos+1, counter+1)

    else:
        # switch with the appropriate index
        prev_num = nums[current_element-1]

        if prev_num == current_element:
            return current_element
        else:
            nums[current_element-1] = current_element
            nums[pos] = prev_num
            print(pos, nums)
            return cycle_sort(nums, pos, counter+1)


class TestMethod(unittest.TestCase):
    def test_base(self):

        base_input = [7, 5, 2, 1, 7, 6, 4, 3]
        base_output = 7

        self.assertEqual(cycle_sort(base_input, 0, 0), base_output)


if __name__ == "__main__":
    unittest.main()
