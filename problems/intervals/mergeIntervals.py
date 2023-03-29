import unittest


def mergeIntervals(arr:list,out_list:list)->list:
    # arr must be sorted in ascending order
    # i must begin from 1 
    l = len(arr)
    # if end of the array  then return 
    if l == 1:
        return out_list
    else:
        m1 = arr.pop(0)
        m2 = arr.pop(0)

        if m1[1] >= m2[0]:
            # merge eligible
            merged = [m1[0],m2[1]]
            arr.insert(0,merged)
            
            if len(out_list)>2:
                out_list.pop() 
            
            out_list.append(merged)
            
            return mergeIntervals(arr,out_list)
        else:
            out_list.append(m2)
            arr.insert(0,m2)
            return mergeIntervals(arr,out_list)
        


class TestMethod(unittest.TestCase):
    def test_base(self):
        test_input = [[3,7],[6,8],[10,12],[11,15], [14,19], [18,23],[20,31]]
        print(mergeIntervals(test_input,out_list=[]))

        
        
        self.assertTrue(False)



if __name__ == "__main__":
    unittest.main()

# reformat : SHIFT + OPTION + F