import unittest
import math

# determine the number of digits in the integer using log10
# must be the absolute value of a given integer.
# modulo % operator returns the remainder after division
# floor division // operator returns the whole floor number after division


def reverseInteger(n:int)->int:
    """
    returns the reverse of an integer
    """

    sign = 1 if n >= 0 else -1 
    
    n_digits = math.floor(math.log10(abs(n)) + 1)
    reversed_int = 0
    
    i = 1
    while i < n_digits+1 :
        reversed_int += abs(n)%10**i // 10**(i-1) * 10**(n_digits-i)
        i+=1
      
    return sign * reversed_int



class TestReverseInteger(unittest.TestCase):

    def test_negative_integer(self):
        test_input = -123
        test_output = reverseInteger(test_input)
        self.assertEqual(-321,test_output)


    def test_trailing_zero(self):
        
        test_input = 1000
        test_output = reverseInteger(test_input)
        self.assertEqual(1,test_output)



if __name__ == "__main__":
    unittest.main()