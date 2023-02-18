from random import choice

class Baralho:
    baralho = []
    naipe = ("copas","paus","ouros","espadas")
    cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    num = 0
    while num < len(cartas):
        for i in cartas:
            num += 1
            if num >= 10:
                v = 10
            else:
                v = num
            for j in naipe:
                carta = {'carta': i,'naipe': j,'valor':v}
                baralho.append(carta)

    def __init__(self):
        self.baralho = Baralho.baralho
        self.carta = None
        self.set_carta()
    
    def set_carta(self):
       carta = choice(self.baralho)
       self.carta = carta

    

cartas = Baralho()
print(cartas.baralho)
print()
print(cartas.carta)