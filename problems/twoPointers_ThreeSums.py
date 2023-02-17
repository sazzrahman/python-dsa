import unittest

# given an array of n integers determine if any set of  3 elements sum to a target
# brute force is to take a subset of 3 numbers and find the sum and match with the target
# the two pointer method sorts the array first and compares low and high values


def compare_sum(arr:list,current:int,low:int,high:int,target:int)->tuple:
    """
    takes a sorted array and recursively finds a triplet that add to a target
    low : current low index
    high: current high index
    target: the value to be matched
    """
    if low>=high:
        # stopping condition
        return None
    print(f"current triplet ({arr[low]},{arr[high]},{arr[current]}) --> {target}")
    current_sum = arr[low] + arr[high] + arr[current]

    if current_sum == target:
        print(f"acceptable combination ({arr[low]},{arr[high]},{arr[current]}) --> {target}")
        return current,low,high
    elif current_sum>target:
        return compare_sum(arr,current,low,high-1,target)
    elif current_sum<target:
        return compare_sum(arr,current,low+1,high,target)


def threeSum(arr:list,target:int) -> bool:
    arr.sort()
    i = 0
    l = len(arr)
    out_list = []
    while i < l:
        low = i+1
        high = l-1
        current_output = compare_sum(arr,i,low,high,target)
        if current_output:
            # find the values 
            values = arr[current_output[0]],arr[current_output[1]],arr[current_output[2]]
            out_list.append(values)
        i+=1
    return out_list

    


class TestThreeSum(unittest.TestCase):
    def test_base(self):
        test_input = [3,7,1,2,8,4,5]
        target = 10
        test_output = threeSum(test_input,target)
        print(test_output)
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()