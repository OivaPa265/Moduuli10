#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

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


talo = Talo(0,10,2)

talo.liikuminen(1,5)
talo.liikuminen(2,6)
talo.liikuminen(1,0)