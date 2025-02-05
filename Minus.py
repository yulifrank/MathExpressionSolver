
from BinExp import BinExp


class Minus(BinExp):
    def calc(self):
        return  self.left.calc() - self.right.calc()