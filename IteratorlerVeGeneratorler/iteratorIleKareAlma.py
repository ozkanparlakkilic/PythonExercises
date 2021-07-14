
class Kareler():

    def __init__(self,max=0):

        self.max = max
        self.sayi = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.sayi <= self.max :

            sonuc = self.sayi ** 2

            self.sayi += 1

            return sonuc
        else:
            raise StopIteration


kareler = Kareler(5)

iterator = iter(kareler)

for i in kareler:
    print(i)