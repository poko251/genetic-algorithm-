import random

class Chromosome:

    """0. KODOWANIE: Zastosowałem kadoowanie binarne, każdego osobnika reprezentuje wektor zer oraz jedynek o długości parametru "chromosomeSize".

    Gdzie ostatni gen: znak (0 = dodatnia, 1 = ujemna), a reszta odpowiada za liczbę naturalną.
    1. Wybór popoulacji początkowej: Wybrałem metodę losowania wartosći ze zbioru {0,1}

    2. Ocena osobników to wartosć funkcji dla danej zmiennej x
    """

    def __init__(self, chromosomeSize):

        #WYBOR POPULACJI POCZĄTKWOEJ
        self.genes = list() #Pusta lista

        for _ in range(chromosomeSize): 
            self.genes.append(random.randint(0,1)) #Dodaje losowe wartosci

        self.value = self.decode() #KODOWANIE
        self.fitness = self.evaluation() #OCENA OSOBNIKOW



    def decode(self):
        """"Metoda która dekoduje osobnika c do zmiennej x"""
        sign = -1 if self.genes[-1] == 1 else 1 #znak

        value = 0 # wartosc
        value_number = len(self.genes) - 1 #ilosc genow odpowiedzialnych za wartosc

        for i in range(value_number):
            
            power = value_number - 1 -i
            value += self.genes[i] * (2 ** power)

        value = value * sign
        return value

    def evaluation(self):
        """Metoda która oblicza wartosc funkcji dla danego osobnika
        funckja: -x^2-2x+10
        """

        return  -1* (self.value**2) - 2 * self.value + 10



    def __str__(self):
        return f"genes:{self.genes}, decoded_value:{self.value}, evaluation:{self.fitness}"

