from __future__ import annotations
from module1 import Vozidlo


class Cesta():
    def __init__(self, soubor):
        self.start = ""
        self.cil = ""
        self.soubor = soubor
        self.vzdalenost = 0
        self.cena_litr_paliva = 0
        self.flotila = []

    def readfile(self):
        file = open(self.soubor, 'r')
        lines = file.readlines()

        self.start = lines[0].strip()
        self.cil = lines[1].strip()
        self.vzdalenost = float(lines[2].strip())       
        """
        vyrobce = lines[3].strip()
        model = lines[4].strip()
        spo = float(lines[5].strip())
        self.pridej_vozidlo(Vozidlo(vyrobce,model,spo))
        vyrobce = lines[6].strip()
        model = lines[7].strip()
        spo = float(lines[8].strip())
        self.pridej_vozidlo(Vozidlo(vyrobce,model,spo))
        """
        
        for i, line in enumerate(lines):
            if i > 2:
                if i % 3 == 0:
                    vyrobce = line.strip()
                if i % 3 == 1:
                    model = line.strip()
                if i % 3 == 2:
                    spo = float(line.strip())
                    self.flotila.append(Vozidlo(vyrobce,model,spo))
        
        file.close()
        

    def show(self):
        print(f"From {self.start} to {self.cil}. Vzdalenost je: {self.vzdalenost}")
        for i, vozidlo in enumerate(self.flotila):
            print(f"Vyrobce je: ", vozidlo.vyrobce)
            print(f"Model je: ", vozidlo.model)
            print(f"Spotrebu je: ", vozidlo.spotreba_l_100)

    def pridej_vozidlo(self,vo):
        self.flotila.append(vo)

    def cena(self, k):
        self.cena_litr_paliva = k

    def Sort(self):
        temp = Vozidlo
        for i in range(len(self.flotila)):
            for j in range(len(self.flotila) - 1):
                if self.flotila[j].sosanh(self.flotila[j + 1]) == False:
                    temp = self.flotila[j]
                    self.flotila[j] = self.flotila[j + 1]
                    self.flotila[j + 1] = temp
    
    def spocitej_celkovou_spotrebu(self):
        celkovou = 0
        for i, vozidlo in enumerate(self.flotila):
            celkovou += vozidlo.get_spotrebu() * self.vzdalenost / 100
        return celkovou
    
    def spocitej_celkovou_cenu(self):
        celkovoucena = 0
        for i, vozidlo in enumerate(self.flotila):
            celkovoucena += vozidlo.get_spotrebu() * self.vzdalenost * self.cena_litr_paliva / 100
        return celkovoucena

    def get_vozidlo(self, index):
        if (index < len(self.flotila)):
            return self.flotila[index]

    def __del__(self):
        self.Sort()
        file = open(self.soubor, 'w')
        file.write(f"{self.start}\n")
        file.write(f"{self.cil}\n")
        file.write(f"{str(self.vzdalenost)}\n")
        for i, vozidlo in enumerate(self.flotila):
            file.write(f"{self.flotila[i].vyrobce}\n")
            file.write(f"{self.flotila[i].model}\n")
            file.write(f"{str(self.flotila[i].get_spotrebu())}\n")
        file.close()

a = Cesta("cesta.txt")
a.readfile()
a.show()
nove_auto = Vozidlo("Ford","Focus", 5.8)
nove_auto.show()
a.pridej_vozidlo(nove_auto)
a.cena(3.2)
a.get_vozidlo(0).calculate_spotrebu(85,4.3)
print(a.spocitej_celkovou_spotrebu())
print(a.spocitej_celkovou_cenu())
del a
            




    
