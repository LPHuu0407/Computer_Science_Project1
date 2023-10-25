import random
from Genetic_Algorithm import *

# Hàm Main()
def Main():
    global Population_Size
    # Thế hệ đâù tiên
    Generation = 1
    Found = False
    Population = []

    # Khởi tạo quần thể ban đầu
    for _ in range(Population_Size):
        Chromosome = Individual.Create_Chromosome() # Gọi hàm "Create_Chromosome" để tạo các nhiễm sắc thể
        Population.append(Individual(Chromosome)) # Thêm các nhiễm sắc thể vào mảng "Population"

    while not Found:
        
