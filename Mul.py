
from BinExp import BinExp


class Mul(BinExp):
    def calc(self):
        return  self.left.calc() * self.right.calc()