

class MathDojo:

    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        if nums is not None:
            self.result += num
            for x in nums:
                self.result += x
        else:
            self.result += num
        return self

    def subtract(self, num, *nums):
        if nums is not None:
            self.result -= num
            for x in nums:
                self.result -= x
        else:
            self.result -= num

        return self

md = MathDojo()

x = md.add(2).add(22,5,10).subtract(3,2,1).result
print(x)


