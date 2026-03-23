#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class hissi:
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.nykyinen = alin

    def kerros_ylos(self):
        if self.nykyinen <self.ylin:
            self.nykyinen +=1
            print(f"kerros: {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen >self.alin:
            self.nykyinen -=1
            print(f"kerros: {self.nykyinen}")

    def siirtyminen(self,tavoite):

            while self.nykyinen != tavoite:

                matka = tavoite - self.nykyinen
                print(f"hissi on {matka} kerrosta tavoiteesta {tavoite} ")

                if self.nykyinen < tavoite:
                    self.kerros_ylos()

                elif self.nykyinen > tavoite:
                    self.kerros_alas()

class Talo:
    def __init__(self, alin, ylin,hissi_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissi_maara):
            uusi_hissi = hissi(ylin,alin)
            self.hissit.append(uusi_hissi)

    def liikuminen(self, hissi_nmr, kohde):
        sinun_hissi= self.hissit[hissi_nmr -1]
        print(f"{hissi_nmr}")
        sinun_hissi.siirtyminen(kohde)

    def paloHalytys(self):
        print("HAAHAA vedin palo halytys vivusta  nyt kaikki hissit palaavat 0 kerrokseen :3")
        print("" + "=" * 30)
        for hissit in self.hissit:
               hissit.siirtyminen(self.alin)

talo = Talo(0,10,2)

talo.liikuminen(1,5)
print("" + "=" * 30)

talo.liikuminen(2,6)
print("" + "=" * 30)

talo.paloHalytys()
print("" + "=" * 30)