class Vozidlo:
    def __init__(self, vyrobce, model, spotreba_l_100):
        self.vyrobce = vyrobce
        self.model = model
        self.spotreba_l_100 = spotreba_l_100

    def sosanh(self, vozidlo):
        if isinstance(vozidlo, Vozidlo):
            if self.spotreba_l_100 < vozidlo.spotreba_l_100:
                return True
        return False

    def show(self):
        print(f"Vyrobce je: ", self.vyrobce)
        print(f"Model je: ", self.model)
        print(f"Spotrebu je: ", self.spotreba_l_100)

    def calculate_spotrebu(self, vzda, spo):
        self.spotreba_l_100 = (spo/vzda) * 100
        return self.spotreba_l_100

    
