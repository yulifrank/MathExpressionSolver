from BinExp import BinExp


class Plus(BinExp):
    def calc(self):
        return  self.left.calc() + self.right.calc()