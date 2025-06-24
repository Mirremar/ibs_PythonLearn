class Animal:
    _count = 0
    def __init__(self):
       Animal._count+=1
        
    def voice(self):
        pass

    @staticmethod
    def getCount():
        return Animal._count


class Wolf(Animal):
    def voice(self):
        return "awoooo"


class Kitten(Animal):
    def voice(self):
        return "mlem"


class Crow(Animal):
    def voice(self):
        return "Karrrr"

wolf = Wolf()
cat = Kitten()
crow = Crow()

print(wolf.voice())
print(cat.voice())
print(crow.voice())
print(Animal.getCount())