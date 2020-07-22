class Animales:

    def __init__(self, organizacion_celular, patas):       
        self.organizacion_celular = organizacion_celular
        self.patas = patas

    def __str__(self):
        return "{}, {}".format(self.organizacion_celular, self.patas)

class Vertebrados(Animales):

    def __init__(self, organizacion_celular, patas, craneo, sistema_oseo):
        super().__init__(organizacion_celular, patas)
        self.craneo = craneo
        self.sistema_oseo = sistema_oseo

    def __str__(self):
        return super().__str__() + "{}, {}".format(self.craneo, self.sistema_oseo)

class Mamiferos(Vertebrados):

    def __init__(self, organizacion_celular, patas, craneo, sistema_oseo, pelo):
        super().__init__(organizacion_celular, patas, craneo, sistema_oseo)
        self.pelo = pelo

    def __str__(self):
        return super().__str__() + "{}".format(self.pelo)

class Invertebrados(Animales):

    def __init__(self, organizacion_celular, patas, estructura_no_esqueletica):
        super().__init__(organizacion_celular, patas)
        self.estructura_no_esqueletica = estructura_no_esqueletica

    def __str__(self):
        return super().__str__() + "{}".format(self.estructura_no_esqueletica)

class Crustaceos(Invertebrados):

    def __init__(self, organizacion_celular, patas, estructura_no_esqueletica, tenazas):
        self.tenazas = tenazas
        super().__init__(organizacion_celular, patas, estructura_no_esqueletica)

    def __str__(self):
        return super().__str__() + "{}".format(self.tenazas)

def run(animal, patas):

    if patas != None:
        counter = 0
        for i in animal:
            if i.patas == patas:
                counter += 1
        print("Se han encontrado {} animales con {} patas:".format(counter, patas))

    for i in animal:
        if patas == None:
            print(type(i).__name__, i)
        else:
            if i.patas == patas:
                print(type(i).__name__, i)


lista = [
    Vertebrados("Pluricelular", 4, "craneo fijo", "vertebral"),
    Mamiferos("Pluricelular", 4, "craneo fijo", "vertebral", "peludos"),
    Invertebrados("Pluricelular", 6, "estructura dinámica"),
    Crustaceos("Pluricelular", 8, "estructura dinámica", "tenazas duras")
]

if __name__ == "__main__":
    # run(lista)
    run(lista, 2)
    run(lista, 6)
    run(lista, 6)
    run(lista, 8)
