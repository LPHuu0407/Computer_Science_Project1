# Gọi thư viện 'random', thư viện 'random' 
# hỗ trợ các hàm trả về các số, chuỗi ngẫu nhiên 
import random

# Biến 'Population_Size' tạo một quần thể 
# có số lượng xác định
Population_Size = 100

# Khai báo 'Genes'
Genes = '''abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789,.-;:_!"#%&/()=?@${[]}'''

# 'Target' sẽ chứa chuỗi mục tiêu muốn đạt được
Target = str(input("Enter target: "))

# Lớp 'Individual'
# Nhiệm vụ tìm ra cá thể tốt nhất
class Individual(object):
    # Hàm __init__ đại diện cho cá thể 
    # trong quần thể các chuỗi mục tiêu
    def __init__(self, Value_Chromosome):
        self.chromosome = Value_Chromosome
        self.fitness = self.Fitness()
    @classmethod
    
    # Hàm 'Genetic_Mutation' được dùng tạo ra các gen đột biến
    def Genetic_Mutation(self):
        global Genes
        Gen = random.choice(Genes)
        return Gen
    @classmethod
    
    # Tạo ra nhiễm sắc thể hoặc một chuỗi
    def Create_Chromosome(self):
        global Target
        Chromosome_Len = len(Target)
        return [self.Genetic_Mutation() for _ in range(Chromosome_Len)]
    @classmethod
    
    # Thực hiện giao phối, sinh ra con cái từ 2 nhiễm sắc thể
    def Mating(self, Parents):
        Child_Chromosome = [] # Tạo mảng chứa các nhiễm sắc thể con
        for Parent_1, Parent_2 in zip(self.chromosome, Parents.chromosome):
            # Tạo xác suất ngẫu nhiên
            Probability = random.random()
            if Probability < 0.45: # Nếu xác suất nhỏ hơn 0.45
                Child_Chromosome.append(Parent_1)
            elif Probability < 0.90: # Nếu xác suất nhỏ hơn 0.90
                Child_Chromosome.append(Parent_2)
            else: # Trường hợp còn lại
                Child_Chromosome.append(self.Genetic_Mutation())
        
        return Individual(Child_Chromosome)
    # def Fitness(self):
    #     global Target
    #     fitness = 0
    #     for 









