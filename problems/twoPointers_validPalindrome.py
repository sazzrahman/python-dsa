import unittest



# check if it is a valid palindrome by removing at most 1 character
# brute force: remove 1 character and check if the remaining string is a palindrome

def validPalindrome(s:str)->bool:
    l = len(s)
    start = 0
    end = l-1
    i = 0
    counter = 0

    while i < l//2 + 1:
        
        if s[start] == s[end]:
            print(s[start],"----moved-both--",s[end])
            start+=1
            end-=1
            
        else:
            if s[start+1]==s[end]:
                counter +=1
                start+=1
                print(s[start],"----moved-start--",s[end])
            elif s[start]==s[end-1]:
                counter+=1
                end-=1
                print(s[start],"----moved-end--",s[end])
            else:
                return False
        i+=1
    if counter>1:
        return False

    return True
    



class TestMethod(unittest.TestCase):
    def test_base(self):
        
        test_input = "raceacar"
        print(validPalindrome(test_input))
        
        self.assertTrue(False)



if __name__ == "__main__":
    unittest.main()