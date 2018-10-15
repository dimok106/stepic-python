class Buffer:
    def __init__(self):
        self.current =[]

    def add(self, *a):
        self.current += a
        while len(self.current)>4:
            fiveEl = self.current[0:5]
            summ = 0;
            for el in fiveEl:
                summ += el
            print(summ)
            self.current= self.current[5:]


    def get_current_part(self):

        return self.current

    def fiveElSumm (self, fiveEl):
        summ = 0;
        for el in fiveEl:
            summ+= el
        return summ
