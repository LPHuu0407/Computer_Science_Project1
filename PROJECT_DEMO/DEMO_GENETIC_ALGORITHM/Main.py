import random
from Genetic_Algorithm import *
# Main Function
def Main():
    global Population_Size
    # Initialize the first generation
    Generation = 1
    Found = False
    Population = []
    # Initiialization
    for _ in range(Population_Size):
        # Call the function "Create_Chromosome" to create chromosomes
        Chromosome = Individual.Create_Chromosome()
        # Add chromosomes to the "Population" array
        Population.append(Individual(Chromosome))
    # Selection
    while not Found:
        # Sort chromosomes in ascending order based on fitness score
        Population = sorted(Population, key = lambda x:x.fitness)
        # If the chromosome has a fitness score of 0 then the target chromosome has been found
        if Population[0].fitness <= 0:
            Found = True
            break
        # Create a new generation and select good individuals into this new position
        New_Generation = []
        # Perform a transfer of 10% of individuals from the current population to the next generation
        Size = int((10 * Population_Size) / 100)
        # Add 10% of the old population's strings to the new population using the extend() function
        New_Generation.extend(Population[:Size])
        # 50% of the 90% of individuals in the current population will undergo 'Crossover'
        Size = int((90 * Population_Size) / 100)
        # Crossover
        for _ in range(Size):
            Parent_1 = random.choice(Population[:50])
            Parent_2 = random.choice(Population[:50])
            Child = Parent_1.Crossover(Parent_2)
            New_Generation.append(Child)
        Population = New_Generation
        print("Generation: {}\tString: {}\tFitness: {}".\
			format(Generation,"".join(Population[0].chromosome),Population[0].fitness))
        Generation += 1
    print("Generation: {}\tString: {}\tFitness: {}".\
			format(Generation,"".join(Population[0].chromosome),Population[0].fitness))
if __name__ == '__main__':
    Main()