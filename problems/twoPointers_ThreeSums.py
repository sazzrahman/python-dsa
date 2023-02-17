import unittest

# given an array of n integers determine if any set of  3 elements sum to a target
# brute force is to take a subset of 3 numbers and find the sum and match with the target
# the two pointer method sorts the array first and compares low and high values

def threeSum(arr:list,target:int) -> bool:
    arr.sort()
    print("sorted array -->",arr)
    l = len(arr)
    
    low = 0
    high = l-1

    for i in range(l):
        low = i + 1
        
        print(i, low, high)
    
    return False

    


class TestThreeSum(unittest.TestCase):
    def test_base(self):
        test_input = [3,7,1,2,8,4,5]
        target = 10
        test_output = threeSum(test_input,target)
        
        self.assertTrue(test_output)






if __name__ == "__main__":
    unittest.main()