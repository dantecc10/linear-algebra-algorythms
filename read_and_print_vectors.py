import fractions_code as frc

def read_vector(dimension=False):
    if dimension == False:
        dimension = int(input("Enter the dimension of the vector: "))
    vector = []
    
    for i in range(dimension):
        vector.append(float(input("Enter the value of the vector at index " + str(i) + ": ")))
        
    return vector

def vectors_reader(quantity=False, dimension=False):
    vectors = []
    
    if quantity == False:
        quantity = int(input("Enter the number of vectors: "))
        
    if dimension == False:
        dimension = int(input("Enter the dimension of the vectors: "))
    
    for i in range(quantity):
        vectors.append(read_vector(dimension=dimension))
    
    return vectors

def vectors_printer(vectors):
    for i in range(len(vectors)):
        print("Vector " + str(i) + ": ")
        vector_str = "v" + str(i) + " = ("
        for k in range(len(vectors[i])):
            if k == len(vectors[i]) - 1:
                vector_str += str(vectors[i][k]) + ")"
            else:
                vector_str += str(vectors[i][k]) + ", "
        print(vector_str)
        print ("")
        
def f_printer_vectors(vectors):
    for i in range(len(vectors)):
        print("Vector " + str(i) + ": ")
        vector_str = "v" + str(i) + " = ("
        for k in range(len(vectors[i])):
            if k == len(vectors[i]) - 1:
                vector_str += str(frc.fraction_val(vectors[i][k])) + ")"
            else:
                vector_str += str(frc.fraction_val(vectors[i][k])) + ", "
        print(vector_str)
        print ("")
        
#f_printer_vectors(vectors_reader())
#read_vector()