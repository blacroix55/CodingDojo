class Underscore:
    def map(self, iterable, callback):
        for i in range(0,len(iterable)):
            iterable[i]=callback(i)
        return iterable

    def find(self, iterable, callback):
        for i in range(0,len(iterable)):
            if callback(iterable[i]):
                return iterable[i]

    def filter(self, iterable, callback):
        ans=[]
        for i in range(0,len(iterable)):
            if callback(iterable[i]):
                ans.append(iterable[i])
        return ans

    def reject(self, iterable, callback):
        ans=[]
        for i in range(0,len(iterable)):
            if not callback(iterable[i]):
                ans.append(iterable[i])
        return ans

# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print ("Evens =",evens)
# should return [2, 4, 6] after you finish implementing the code above

odds = _.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
print ("Odds =",odds)

mult = _.map([1,2,3], lambda x: x*2) # should return [2,4,6]
print ("mult =",mult)

greaterThan4 = _.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
print ("First greater than 4 =",greaterThan4)
