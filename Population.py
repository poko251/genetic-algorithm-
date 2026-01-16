from Chromosome import Chromosome

class Population:
    """Populacja początkowa, S(0), składającego sie z k osobników (poplationSize)"""
    def __init__(self, populationSize, chromosomeSize):
    
        self.chromosomes = list() #lsta wszystkich osobnikow
        
        #dodaje k razy nowego osobnika
        for _ in range(populationSize):
            chromosome = Chromosome(chromosomeSize)#nowy osobnik
            self.chromosomes.append(chromosome)


    def evaluationForALL(self): #liczy wartosc funckje dla calej populacji
        for chromosome in self.chromosomes:
            current_fitness = chromosome.evaluation()
            total_fitness += current_fitness

        #srednia ocena popualacji  
        average_fitness = total_fitness / len(self.chromosomes)
        return average_fitness


    def sortFittest(self, n): #sortuje osobniki wzgledem, wartosci funckji, (przydaje sie do elitarnej selekcji) zwraca top n wynikow
        self.chromosomes.sort(key=lambda x:x.evaluation())
        return self.chromosomes[:n]
        
        

    def show_population(self): #pokazuje populacje
        for i, c in enumerate(self.chromosomes):
            print(f"index:{i}   :{c}")
