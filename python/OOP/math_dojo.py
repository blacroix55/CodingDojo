class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        if nums:
            for n in nums:
                self.result += n
        return self
    def subtract(self, num, *nums):
        self.result -= num
        if nums:
            for n in nums:
                self.result -= n
        return self

# create an instance:
md = MathDojo()

# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

# run each of the methods a few more times and check the result!
brian = MathDojo() # runs __init__, which in this case sets brian.result to 0
y = brian.add(5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1).subtract(1,1,1,1,1,1,1,1,1,1).add(1,2,3).subtract(1,2,3).result
print (y)