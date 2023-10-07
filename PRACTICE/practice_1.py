# Python3 program to create target string, starting from
# random string using Genetic Algorithm
import random

# Number of individuals in each generation
POPULATION_SIZE = 100

# Valid genes
GENES = '''bacdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.-;:_!"#%&/()=?@${[]}'''

# Target string to be generated
TARGET = str(input("Enter target: "))

class Individual(object):
	# Class representing individual in population
	# Lớp đại diện cho cá thể trong quần thể
	def __init__(self, chromosome):
		self.chromosome = chromosome
		self.fitness = self.cal_fitness()

	@classmethod
	def mutated_genes(self):
		# Create random genes for mutation
		# Tạo gen ngẫu nhiên để đột biến
		global GENES
		gene = random.choice(GENES)
		return gene

	@classmethod
	def create_gnome(self):
		# Create chromosome or string of genes
		# Tạo ra nhiễm sắc thể hoặc chuỗi gen
		global TARGET
		gnome_len = len(TARGET)
		return [self.mutated_genes() for _ in range(gnome_len)]

	def mate(self, par2):
		# Perform mating and produce new offspring
		# Thực hiện giao phối và sinh ra con cái mới
		# Chromosome for offspring
        # Nhiễm sắc thể cho con cái

		child_chromosome = []
		for gp1, gp2 in zip(self.chromosome, par2.chromosome):	

			# random probability
            # xác suất ngẫu nhiên
			prob = random.random()

			# if prob is less than 0.45, insert gene
            # nếu prob nhỏ hơn 0,45 thì chèn gen vào

			# from parent 1
			if prob < 0.45:
				child_chromosome.append(gp1)

			# if prob is between 0.45 and 0.90, insert
            # nếu thăm dò nằm trong khoảng từ 0,45 đến 0,90, hãy chèn
			# gene from parent 2
			elif prob < 0.90:
				child_chromosome.append(gp2)

			# otherwise insert random gene(mutate),
			# for maintaining diversity
            # mặt khác chèn gen ngẫu nhiên (đột biến), để duy trì sự đa dạng
			else:
				child_chromosome.append(self.mutated_genes())

		# create new Individual(offspring) using
		# generated chromosome for offspring
        # tạo Cá thể mới (con cái) bằng cách sử dụng nhiễm sắc thể được tạo ra cho con cái
		return Individual(child_chromosome)

	def cal_fitness(self):
		# Calculate fitness score, it is the number of
		#  characters in string which differ from target string.
		# Tính điểm thể lực, đó là số ký tự trong chuỗi khác với chuỗi đích.
		global TARGET
		fitness = 0
		for gs, gt in zip(self.chromosome, TARGET):
			if gs != gt: fitness+= 1
		return fitness

# Driver code
def main():
	global POPULATION_SIZE

	#current generation
	generation = 1

	found = False
	population = []

	# create initial population
    # tạo dân số ban đầu
	for _ in range(POPULATION_SIZE):
				gnome = Individual.create_gnome()
				population.append(Individual(gnome))

	while not found:

		# sort the population in increasing order of fitness score
		population = sorted(population, key = lambda x:x.fitness)

		# if the individual having lowest fitness score ie.
		# 0 then we know that we have reached to the target
		# and break the loop
		if population[0].fitness <= 0:
			found = True
			break

		# Otherwise generate new offsprings for new generation
		new_generation = []

		# Perform Elitism, that mean 10% of fittest population
		# goes to the next generation
		s = int((10*POPULATION_SIZE)/100)
		new_generation.extend(population[:s])

		# From 50% of fittest population, Individuals
		# will mate to produce offspring
		s = int((90*POPULATION_SIZE)/100)
		
		for _ in range(s):
			parent1 = random.choice(population[:50])
			parent2 = random.choice(population[:50])
			child = parent1.mate(parent2)
			new_generation.append(child)

		population = new_generation

		print("Generation: {}\tString: {}\tFitness: {}".\
			format(generation,
			"".join(population[0].chromosome),
			population[0].fitness))

		generation += 1

	
	print("Generation: {}\tString: {}\tFitness: {}".\
		format(generation,
		"".join(population[0].chromosome),
		population[0].fitness))

if __name__ == '__main__':
	main()