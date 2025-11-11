class Expression:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print("Result:", self.a + self.b + self.c)

obj = Expression(5, 10, 15)
obj.add()
