# classes

class Counter:
    """Counter"""
    _i = 1
    def __init__(self, initial = 0):
        self.value = initial
    
    def increment(self):
        self.value += 1
    
    def get(self):
        return self.value

c = Counter(42)
c.increment()
print(c.get())
# print(Counter.__bases__[0])
print(Counter.__dict__)