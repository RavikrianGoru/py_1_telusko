class TopN:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __iter__(self):
        return self

    def __next__(self):
        if self.m1 <= self.m2:
            val = self.m1
            self.m1 = val + 1
            return val
        else:
            raise StopIteration


t = TopN(1,10)
for i in iter(t):
    print(i)
