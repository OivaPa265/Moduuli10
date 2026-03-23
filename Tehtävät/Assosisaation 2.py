#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class hissi:
        #Tekee luokan hissi joss on ylin ja alin hissit
    def __init__(self, ylin, alin):
        self.ylin = ylin
        self.alin = alin
        self.nykyinen = alin
 # siirtää hissiä ylemmäs yksi kerallaan jos hissi on alempi kuin tavoite
    def kerros_ylos(self):
        if self.nykyinen <self.ylin:
            self.nykyinen +=1
            print(f"kerros: {self.nykyinen}")
# siirtää hissiä alemmas yksi kerallaan jos hissi on suurempi kuin tavoite
    def kerros_alas(self):
        if self.nykyinen >self.alin:
            self.nykyinen -=1
            print(f"kerros: {self.nykyinen}")

# siirtyminen
    def siirtyminen(self,tavoite):

            while self.nykyinen != tavoite:
             # näytää kerrosten määrän kunnes hissi on tavoitteessa
                matka = tavoite - self.nykyinen
                print(f"hissi on {matka} kerrosta tavoiteesta {tavoite} ")
                # jos hissi on alempi kuin tavoite kutsuu ylös funktion
                if self.nykyinen < tavoite:
                    self.kerros_ylos()
                 # sama mutta alas
                elif self.nykyinen > tavoite:
                    self.kerros_alas()


# ------Tässä on 2 tehtävän asiat-----------

# tekee talo luokan jossa ylin ja alin hissi sekä hissien määrä
class Talo:
    def __init__(self, alin, ylin,hissi_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

           # laskee hissjen määrän
        for i in range(hissi_maara):
            uusi_hissi = hissi(ylin,alin)
            self.hissit.append(uusi_hissi)
         # liikutaa hissejä
    def liikuminen(self, hissi_nmr, kohde):

        sinun_hissi= self.hissit[hissi_nmr -1]
        print(f"{hissi_nmr}")
        sinun_hissi.siirtyminen(kohde)

# päätää talon alimman ja ylimmäbn kerroksen sekä hissien määrän
talo = Talo(0,10,2)

print("" + "=" * 30)
# liikutaa hissiä numero 1 
talo.liikuminen(1,5)
print("" + "=" * 30)
# liikutaa hissiä numero 2
talo.liikuminen(2,6)
print("" + "=" * 30)
