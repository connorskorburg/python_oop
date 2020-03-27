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

x = md.add(15).add(10,25,50).add(50,50,100).subtract(50).subtract(50,25,25).subtract(50, 50, 30, 10).result #result: 5

print(x)