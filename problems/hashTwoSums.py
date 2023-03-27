# reformat : SHIFT + OPTION + F
import unittest

# given an array find all possible pairs of integers that add to a target value.
# return the index of the pairs
# every iteration, we check if the current item is in the hash 
# and the target-item is in the hash map as well. 

def twoSums(arr:list,target:int, return_index=True)->list:
    
    hash = {}
    out_list = []
    i = 0
    l = len(arr)
    while i < l:
        current_num = arr[i]
        alternate_num = abs(target-current_num)

        # check if current number in hash
        # if not add it to hash
        if current_num not in hash:
            hash[current_num] = i

        # then check if alternate is in the hash
        # if not, then continue, do nothing 
        if alternate_num in hash:
            p1 = hash.get(current_num)
            p2 = hash.get(alternate_num)

            if return_index:
                out_list.append((p1,p2))
            else:
                out_list.append((current_num,alternate_num))
        i+=1
    return out_list
    


class TestMethod(unittest.TestCase):
    def test_base(self):

        input_arr = [1,9,6,7,3,4,10,9,2]
        input_target = 11
        
        print(twoSums(input_arr,input_target,return_index=False))
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()