from GeneticAlgoritm import GeneticAlgoritm

algorytm = GeneticAlgoritm(populationSize=100, chromosomeSize=10, elitismSize=40, epsilon=0.001)


najlepszy = algorytm.run(epsilon=0.001, maxGenerations=1000)

print(najlepszy)