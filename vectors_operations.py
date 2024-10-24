import read_and_print_vectors as rpv

def point_product(vector1=False, vector2=False):
    length = 0
    if vector1 == False:
        if length == 0:
            length = int(input("Enter the dimension of the vectors: "))
        vector1 = rpv.read_vector(length)
        
    if vector2 == False:
        if length == 0:
            length = int(input("Enter the dimension of the vectors: "))
        vector2 = rpv.read_vector(length)
    
    if len(vector1) != len(vector2):
        return "The vectors must have the same dimension"
    
    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
        
    return result

def add_vectors(vector1=False, vector2=False):
    length = 0
    if vector1 == False:
        if length == 0:
            length = int(input("Enter the dimension of the vectors: "))
        vector1 = rpv.read_vector(length)
        
    if vector2 == False:
        if length == 0:
            length = int(input("Enter the dimension of the vectors: "))
        vector2 = rpv.read_vector(length)
    
    if len(vector1) != len(vector2):
        return "The vectors must have the same dimension"
    
    result = []
    for i in range(len(vector1)):
        result.append(vector1[i] + vector2[i])
        
    return result

def scalar_product(vector, scalar):
    result = []
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
        
    return result

# print(point_product())