class Animal:
    def voice(self):
        pass


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