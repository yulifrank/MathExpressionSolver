
from BinExp import BinExp


class Div(BinExp):
    def calc(self):
        return  self.left.calc() / self.right.calc()