from Expression import Expression


class Num(Expression):
    def __init__(self,value):
        self.value = value
    def calc(self):
        return self.value
