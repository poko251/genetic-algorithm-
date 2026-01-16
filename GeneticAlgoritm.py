import random
from Chromosome import Chromosome

class GeneticAlgoritm:
    """Selekcja: Wybrałem metode (kola) ruletki oraz elitarna
    Krzyżowanie: Wybralem krzyzowanie jednopuntkowe
    Mutacja: Dla kazdego genu w kazdym osobniku losowana jest wartosc d z przedzialu [0,1] jesli d <= od prawdopodobienstwa mutacji to wartosc zmieniam na przeciwna p_m = 0,01
    """

    def __init__(self, populationSize, chromosomeSize, elitismSize, mutationRate):
        self.populationSize = populationSize
        self.chromosomeSize = chromosomeSize
        self.eltisimSize = elitismSize
        self.mutationRate = mutationRate
        


    def eltisimSelection(self, elitismSize, population): #selekcja elitarna, wybiera k najlepszych osobnikow
        selected = population.sortFittest(elitismSize)
        return selected


    def rouletteSelection(self, population, count): #selekcja ruletki
        total_fitness = 0
        for chromosome in population.chromosomes: #licze sume wszyskich wartosci funckji
            total_fitness += chromosome.fitness

        selected = list()

        for _ in range(count):
            #liczba d z przedzialu 0,1
            d = random.uniform(0, 1)
            cumulative_sum = 0
            
            for chromosome in population.chromosomes:
                #przedział p_i dla osobnika 
                probability = chromosome.fitness / total_fitness
                cumulative_sum += probability
                
                #jeśli wylosowana wartość d wpadnie w przedział osobnika 
                if d <= cumulative_sum:
                    # Dodajemy osobnika
                    selected.append(chromosome)
                    break
        return selected
        

    def crossOver(self, parent1, parent2, crossoverRate=0.5): #krzyzowanie jednopunkowe

        d = random.uniform(0,1) #czy osobniki bedzie krzyzowane
        
        if d <= crossoverRate: #jesli tak to wybieam punkt krzyzowania

            point  = random.randint(1, self.chromosomeSize-2)
            """tu jest taki dziwny przezial poniewaz nie chce aby caly material sie zamienil daltego
              od 1 do -1, ale koniec przedzialu zmienszam jeszcze o -1 ponieawz chce aby znak zostal taki sam"""

            #dzieci po krzyzowaniu
            child1_genes = parent1.genes[:point] + parent2.genes[point:]
            child2_genes = parent2.genes[:point] + parent1.genes[point:]

            child1 = Chromosome(self.chromosomeSize)
            child1.genes = child1_genes
            child2 = Chromosome(self.chromosomeSize)
            child2.genes = child2_genes

        else:
            #w przeciwnym nic nie zmieniam
            child1 = Chromosome(self.chromosomeSize)
            child1.genes = parent1.genes.copy()
            child2 = Chromosome(self.chromosomeSize)
            child2.genes = parent2.genes.copy()

        #nowe wartosci dzieci
        child1.x = child1.decode()
        child1.fitness = child1.evaluate()
        child2.x = child2.decode()
        child2.fitness = child2.evaluate()

        return child1, child2

    def mutation():
        pass