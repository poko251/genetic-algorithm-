from GeneticAlgoritm import GeneticAlgoritm
import matplotlib.pyplot as plt
import numpy as np

algorytm = GeneticAlgoritm(populationSize=100, chromosomeSize=7, elitismSize=2, epsilon=0.001)


najlepszy = algorytm.run(epsilon=0.001, maxGenerations=100) #zwraca zdekodowaną wartość



def vis(point): #wizualizacja najlepszego osobnika z ostatniej populacji, na wykresie funkcji

    x = np.linspace(-50, 50)
    
    y = -1*(x**2) - 2*(x) + 10

    y_point = -1*(point**2) - 2*(point) + 10

    plt.scatter(point, y_point, color="red")


    plt.axhline(0, color="black")
    plt.axvline(0, color="black")

    plt.plot(x, y)
    plt.show()


vis(najlepszy)