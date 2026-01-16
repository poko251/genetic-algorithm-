import random
from Chromosome import Chromosome
from Population import Population

class GeneticAlgoritm:
    
    """
    3. Warunek stopu: Ocena czy biezaca populacji niewystarczająco rozni sie od poprzedniej populacji - prog to epsilon

    4. Selekcja: Wybrałem metode (kola) ruletki oraz elitarna

    5. Krzyżowanie: Wybralem krzyzowanie jednopuntkowe

    6. Mutacja: Dla kazdego genu w kazdym osobniku losowana jest wartosc d z przedzialu [0,1] jesli d <= od prawdopodobienstwa mutacji to wartosc zmieniam na przeciwna p_m = 0,01
    """

    def __init__(self, populationSize, chromosomeSize, elitismSize, epsilon):
        self.populationSize = populationSize
        self.chromosomeSize = chromosomeSize
        self.elitismSize = elitismSize #ilosc osobnikow elitarnej selekcji
        self.epsilon = epsilon #prog do warunku stopu
        


    def eltisimSelection(self, population):
        """selekcja elitarna, wybiera k najlepszych osobnikow"""
        population.sortFittest()

        #zwraca liste najelszych osobnikow
        return population.chromosomes[:self.elitismSize]


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

        d = random.uniform(0,1) 
        
        if d <= crossoverRate: #czy osobniki bedzie krzyzowane, jesli tak to wybieam punkt krzyzowania

            point  = random.randint(1, self.chromosomeSize-2)
            """tu jest taki dziwny przezial poniewaz nie chce aby caly material sie zamienil daltego
              od 1 do -1, ale koniec przedzialu zmienszam jeszcze o 1 ponieawz chce aby znak zostal taki sam"""

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
        child1.value = child1.decode() 
        child1.fitness = child1.evaluation()
        child2.value = child2.decode() 
        child2.fitness = child2.evaluation()

        return child1, child2

    def mutation(self, population, mutationRate=0.01): #mutacja
            for chromosome in population.chromosomes: #petla po osobnikach
                mutated = False
                for i in range(self.chromosomeSize):  #petla po genach
                    if random.uniform(0, 1) <= mutationRate:
                        chromosome.genes[i] = 1 if chromosome.genes[i] == 0 else 0
                        mutated = True
                
                if mutated:
                    chromosome.value = chromosome.decode()
                    chromosome.fitness = chromosome.evaluation()


    def run(self, epsilon, maxGenerations):

        current_population = Population(self.populationSize, self.chromosomeSize)

        n = 0

        prev_avg_fitness = 0 #srednia wartosc populacji (potrzebne do warunku stopu)

        while n < maxGenerations:
            
            current_avg_fitness = current_population.evaluationForALL() #obenca srednia wartosc populacji

            current_population.sortFittest()
            best_in_population = current_population.chromosomes[0] #najlepszy w danej populacji


            print(f"Pokolenie {n} , Średni Fitness: {current_avg_fitness:.4f} , "
                  f"Najlepszy x: {best_in_population.value:.4f} (f(x): {best_in_population.fitness:.4f})")
            
            #Warunek stopu

            if n > 0:
                if abs(current_avg_fitness - prev_avg_fitness) <= epsilon:
                    print(f"STOP: BRAK WYSTARCZAJĄCEGO ZRÓŻNICOWANIA")
                    break
            prev_avg_fitness = current_avg_fitness

            #nowe pokolenie
            new_chromosomes = list()

            #selekcja elitarna

            elite = self.eltisimSelection(current_population)
            new_chromosomes.extend(elite)

            # selekcja ruletkowa i krzyzowanie

            while len(new_chromosomes) < self.populationSize:

                #selekcja ruletkowa

                parents = self.rouletteSelection(current_population, 2)

                #krzyzowanie 

                child1, child2 = self.crossOver(parents[0], parents[1])

                new_chromosomes.append(child1)

                if len(new_chromosomes) < self.populationSize: #sprawdzam czy jest miejsce na drugie dziecko w populacji
                    new_chromosomes.append(child2)

            current_population.chromosomes = new_chromosomes #nowe chromosomy to nowe pokolenie


            #mutacja
            self.mutation(current_population)

            n += 1

            current_population.evaluationForALL()
            current_population.sortFittest()

        return current_population.chromosomes[0]
            


