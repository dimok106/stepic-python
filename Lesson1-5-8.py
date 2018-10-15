class MoneyBox:




    def __init__(self, capacity):
        self.capacity = capacity;
        self.coins_inside =0
    def can_add(self, v):
        if(self.capacity>=self.coins_inside+v) :
            return True
        else :
            return False

    def add(self, v):
        if self.can_add(v) :
            self.coins_inside +=v
