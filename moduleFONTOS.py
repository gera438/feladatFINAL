#class Eleje
class kerdesek:
    def __init__(self, v):
        data = v.split(";")
        self.kerdes = data[0]
        self.valasz1 = data[1]
        self.valasz2 = data[2]
        self.valasz3 = data[3]
        self.pont1 = data[4]
        self.pont2 = data[5]
        self.pont3 = data[6]

    def Pontok(self, valasz):
        if valasz == "a":
            return self.pont1
        elif valasz == "b":
            return self.pont2
        elif valasz == "c":
            return self.pont3
        else:
            return 0
#class-

#Kérdések Beolvasása
def KerdesBeolvasas():
    kerdesek_file = open("kerdesek.txt","r",encoding="UTF8")
    lista = []
    for i in kerdesek_file:
        lista.append(kerdesek(i))
    return lista
#-

#Válaszok Beolvasása
def ValaszBeolvas():
    valasz = open("valaszok.txt","r",encoding="UTF8")
    lista = []
    for i in valasz:
        lista.append(i)
    return lista
#Válaszok-

