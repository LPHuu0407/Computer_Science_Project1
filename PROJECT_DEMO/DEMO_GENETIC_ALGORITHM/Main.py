import random
from Genetic_Algorithm import *
# Hàm Main()
def Main():
    global Population_Size
    # Khởi tạo thế hệ đâù tiên
    Generation = 1
    Found = False
    Population = []
    # Initiialization
    for _ in range(Population_Size):
        # Gọi hàm "Create_Chromosome" để tạo các nhiễm sắc thể
        Chromosome = Individual.Create_Chromosome()
        # Thêm các nhiễm sắc thể vào mảng "Population"
        Population.append(Individual(Chromosome))
    # Selection
    while not Found:
        # Sắp xếp các nhiễm sắc thể theo thứ tự tăng dần dựa trên điểm thích nghi
        Population = sorted(Population, key = lambda x:x.fitness)
        # Nếu NST có điểm thích nghi bằng 0, thì đã tìm ra NST mục tiêu
        if Population[0].fitness <= 0:
            Found = True
            break
        # Nếu chưa tìm ra NST, thì tạo ra con cái mới cho thế hệ mới
        New_Generation = []
        # Thực hiện quá trình chuyển 10% cá thể từ quần thể hiện hành sang thế thệ tiếp theo
        Size = int((10 * Population_Size) / 100)
        # Thêm 10% chuỗi của quần thể cũ vào quần thể mới bằng hàm extend()
        New_Generation.extend(Population[:Size])
        # 50% cá thể có độ thích nghi cao nhất sẽ được giao phối và sinh ra con cái
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
    Main()huu
