import unittest
class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self
md = MathDojo()
md1 = MathDojo()
x = md.add(15).add(10,25,50).add(50,50,100).subtract(50).subtract(50,25,25).subtract(50, 50, 30, 10).result #result: 10
y = md1.add(50).add(10,15,100).subtract(100, 25).result
print(x)
print(y)

class MathDojoTest(unittest.TestCase):
    def testOne(self):
        self.assertEqual(x, 10)
    def testTwo(self):
        self.assertEqual(y, 50)
    def setUp(self):
        print("Running Tests...")


if __name__ == '__main__':
    unittest.main()