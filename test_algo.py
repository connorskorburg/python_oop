import unittest
#reverse list
def reverse(arr):
    length = len(arr)
    for i in range(1, int(length/2) + 1, 1):
        temp = arr[i - 1]
        arr[i - 1] = arr[length - i]
        arr[length - i] = temp
    return arr
reverse([1,2,3,4,5])

class ReverseTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual( reverse([1,2,3,4,5]), [5,4,3,2,1])
    def testTwo(self):
        self.assertNotEqual(reverse([1,2,3,4,5]), [1,2,3,4,5])
    def testThree(self):    
        self.assertEqual(reverse([5,4,3,2,1,0]), [0,1,2,3,4,5])

def IsPalindrome(word):
    length = len(word)
    if length % 2 == 0:
        first_half = word[:int(length/2)][::-1]
        second_half = word[int(length/2):]
        if first_half == second_half:
            return True
        else:
            return False
    elif length % 2 == 1:
        first_half = word[int(length/2) + 1:]
        second_half = word[:int(length/2)][::-1]
        if first_half == second_half:
            return True
        else:
            return False
        print(second_half)
IsPalindrome("racecar")
# IsPalindrome("noon")
class PalindromeTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(IsPalindrome("racecar"), True)
    def testTwo(self):
        self.assertEqual(IsPalindrome("noon"), True)
    def testThree(self):
        self.assertTrue(IsPalindrome("racecar"))
    def testFour(self):
        self.assertFalse(IsPalindrome("Wrong"))
    def testFive(self):
        self.assertEqual(IsPalindrome("wrong"), False)

def coin(cents):
    quarter = 0;
    dime = 0;
    nickle = 0;
    penny = 0;
    while cents > 0:
        if cents >= 25:
                cents -= 25
                quarter += 1
        elif cents >= 10:
                cents -= 10
                dime += 1
        elif cents >= 5:
                cents -= 5
                nickle += 1
        elif cents >= 1:
                cents -= 1
                penny += 1
    arr = [quarter, dime, nickle, penny]
    print(arr)
    return arr
coin(87)

class CoinTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coin(87), [3,1,0,2])
    def testTwo(self):
        self.assertEqual(coin(1), [0,0,0,1])
    def testThree(self):
        self.assertNotEqual(coin(10), [0,0,0,0])
    def testFour(self):
        self.assertEqual(coin(25), [1,0,0,0])
    def testFive(self):
        self.assertNotEqual(coin(25), [0,0,0,1])

if __name__ == '__main__':
    unittest.main() # this runs our tests