# Import the “random” module, the “random” is module supports return random numbers, characters
import random
# The variable 'Population_Size' creates a population of the specified number
Population_Size : int = 100
# Declare variable 'Genes'
Genes = '''aáàảãạâấầẩẫậăắằẳẵặ bcd đ eéèẻẽẹ êếềểễệ
           fgh iíìỉĩị jklmn oóòỏõọơớờởỡợôốồổỗộ pq
           rst uúùủũụưứừửữự vwx yýỳỷỹỵ z AÁÀẢÃẠÂẤ
           ẦẨẪẬĂẮẰẲẴẶ BCD Đ EÉÈẺẼẸ ÊẾỀỂỄỆ FGH IÍÌ
           ỈĨỊ JKLMN OÓÒỎÕỌƠỚỜỞỠỢÔỐỒỔỖỘ PQRST UÚÙ
           ỦŨỤƯỨỪỬỮỰ VWX YÝỲỶỸỴ Z0123456789,.-;:_
           !"#%&/()=?@${[]}'''
# The variable 'Target' contains the random string to enter
Target = str(input("Enter target: "))
class Individual(object):
    # The __init__ function represents an individual in a population
    def __init__(self, Value_Chromosome):
        self.chromosome = Value_Chromosome
        self.fitness = self.Fitness()
    @classmethod
    # The 'Gene Mutation' function is used to create mutated genes
    def Gene_Mutation(self):
        global Genes
        Gen = random.choice(Genes)
        return Gen
    @classmethod
    # Create chromosomes
    def Create_Chromosome(self):
        global Target
        Chromosome_Len = len(Target)
        return [self.Gene_Mutation() for _ in range(Chromosome_Len)]
    # Create a new chromosome by the 'Crossover' function
    def Crossover(self, Parents):
        # Create an array containing the child chromosomes
        Child_Chromosome = [] 
        for Parent_1, Parent_2 in zip(self.chromosome, Parents.chromosome):
            # Generate random probabilities
            Probability = random.random()
            # If probability is less than 0.45, insert Parent_1's gene
            if Probability < 0.45:
                Child_Chromosome.append(Parent_1)
            # If the probability is between 0.45 - 0.90, insert Parent_2's gene
            elif Probability < 0.90:
                Child_Chromosome.append(Parent_2)
            # The remaining case is a genetic mutation using the "Gene_Mutation" function
            else: 
                Child_Chromosome.append(self.Gene_Mutation())
        # Returns the child chromosome
        return Individual(Child_Chromosome)
    # Evaluate the fitness of the chromosome, compared to the target sequence
    def Fitness(self):
        global Target
        fitness = 0
        for fitness_Chromosome, fitness_Target in zip(self.chromosome, Target):
            if fitness_Chromosome != fitness_Target:
                fitness += 1
        return fitness