from Expression import Expression


class BinExp(Expression):
    def __init__(self , left, right):
        self.left = left
        self.right = right
