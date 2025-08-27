class Animal():
    def __init__(self, vertebra, tipo, subtipo):
        self.vertebra = vertebra
        self.tipo = tipo
        self.subtipo = subtipo

    def mostrarInformacao(self):
        return self.vertebra, self.tipo, self.subtipo

class Vertebrado(Animal):
    def __init__(self, tipo, subtipo):
        super().__init__('Vertebrado', tipo, subtipo)
        self.tipo = tipo
        self.subtipo = subtipo

class Ave(Vertebrado):
    def __init__(self, subtipo):
        super().__init__('Ave', subtipo)
        self.subtipo = subtipo

class Mamifero(Vertebrado):
    def __init__(self, subtipo):
        super().__init__('Mamifero', subtipo)
        self.subtipo = subtipo


class Invertebrado(Animal):
    def __init__(self, tipo, subtipo):
        super().__init__('Invertebrado', tipo, subtipo)
        self.tipo = tipo
        self.subtipo = subtipo

class Inseto(Invertebrado):
    def __init__(self, subtipo):
        super().__init__('Inseto', subtipo)
        self.subtipo = subtipo

class Anelideo(Invertebrado):
    def __init__(self, subtipo):
        super().__init__('Anelideo', subtipo)
        self.subtipo = subtipo

aguia = Ave('Carnivoro')
pomba = Ave('Onivoro')

homem = Mamifero('Onivoro')
vaca = Mamifero('Herbivoro')

pulga = Inseto('Hematofago')
lagarta = Inseto('Herbivoro')

sanguessuga = Anelideo('Hematofago')
minhoca = Anelideo('Onivoro')

x = input("Seu animal é vertebrado ou invertebrado? ")
y = input("Seu animal é ave, mamifero, inseto ou anelideo? ")
z = input("Seu animal é carnivoro, onivoro, herbivoro ou hematofago? ")

if x.lower() == aguia.vertebra.lower() and y.lower() == aguia.tipo.lower() and z.lower() == aguia.subtipo.lower():
    print("Seu animal é uma Águia: "+str(aguia.mostrarInformacao()))

elif x.lower() == pomba.vertebra.lower() and y.lower() == pomba.tipo.lower() and z.lower() == pomba.subtipo.lower():
    print("Seu animal é uma Pomba: "+str(pomba.mostrarInformacao()))

elif x.lower() == homem.vertebra.lower() and y.lower() == homem.tipo.lower() and z.lower() == homem.subtipo.lower():
    print("Seu animal é um Homem: "+str(homem.mostrarInformacao()))

elif x.lower() == vaca.vertebra.lower() and y.lower() == vaca.tipo.lower() and z.lower() == vaca.subtipo.lower():
    print("Seu animal é uma Vaca: "+str(vaca.mostrarInformacao()))

elif x.lower() == pulga.vertebra.lower() and y.lower() == pulga.tipo.lower() and z.lower() == pulga.subtipo.lower():
    print("Seu animal é uma Pulga: "+str(pulga.mostrarInformacao()))

elif x.lower() == lagarta.vertebra.lower() and y.lower() == lagarta.tipo.lower() and z.lower() == lagarta.subtipo.lower():
    print("Seu animal é uma Lagarta: "+str(lagarta.mostrarInformacao()))

elif x.lower() == sanguessuga.vertebra.lower() and y.lower() == sanguessuga.tipo.lower() and z.lower() == sanguessuga.subtipo.lower():
    print("Seu animal é um Sanguessuga: "+str(sanguessuga.mostrarInformacao()))

elif x.lower() == minhoca.vertebra.lower() and y.lower() == minhoca.tipo.lower() and z.lower() == minhoca.subtipo.lower():
    print("Seu animal é uma Minhoca: "+str(minhoca.mostrarInformacao()))