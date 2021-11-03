class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        return v + self.count <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count += v


x = MoneyBox(15)
print(x.capacity)
x.add(16)
print(x.can_add(16))
