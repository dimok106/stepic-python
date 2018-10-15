class ExtendedStack(list):
    def sum(self):
        if len(self)>1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1+top2)

    def sub(self):
        if len(self)>1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1-top2)
        # операция вычитания

    def mul(self):
        if len(self)>1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1*top2)
        # операция умножения

    def div(self):
        if len(self)>1:
            top1 = self.pop()
            top2 = self.pop()
            self.append(top1//top2)
        # операция целочисленного деления
