import fractions_code as frc
import read_and_print_matrices as rpm
import read_and_print_vectors as rpv
import vectors_operations as vop

def create_gauss_matrix(matrix = False):
    if matrix == False:
        dimension = int(input("Enter the dimension of the matrix: "))
        temp_matrix = rpm.read_matrix(dimension, dimension)
    else:
        temp_matrix = matrix
    
    for i in range(len(temp_matrix)):
        temp_matrix[i].append(0)
    return temp_matrix

def print_gauss_matrix(matrix):
    print("┌")
    for i in range(len(matrix)):
        row_str = "| "
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                row_str += "| " + str(frc.fraction_val(matrix[i][j]))
            else:
                row_str += str(frc.fraction_val(matrix[i][j])) + " "
        row_str += " |"
        print(row_str)
    print("└")

gauss_amplified_sample_matrix = [
    [1, 2, 3, 0],
    [4, 5, 6, 0],
    [7, 8, 9, 0]
]

def zeros_column(matrix, col):
    zeros_col = True
    non_zero_vals = []
    for i in range(len(matrix)):
        if matrix[i][col] != 0:
            zeros_col = False
            non_zero_vals.append(i)
            break
    return [zeros_col, non_zero_vals]

def gauss_matrix_solver(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        pivot = matrix[i][i]

        # Si el pivote es cero, buscamos una fila para intercambiar
        if pivot == 0:
            zeros_check = zeros_column(matrix, i)
            if zeros_check[0]:
                return "Impossible to solve this matrix!"
            else:
                # Intercambiamos la fila actual con la fila que tiene un valor no cero
                matrix[i], matrix[zeros_check[1][0]] = matrix[zeros_check[1][0]], matrix[i]
                pivot = matrix[i][i]  # Actualizar el pivote después del intercambio

        # Normalizamos la fila del pivote (hacemos que el pivote sea 1)
        matrix[i] = [x / pivot for x in matrix[i]]

        # Eliminamos los elementos en las otras filas usando operaciones de fila
        for j in range(rows):
            if j == i:
                continue
            factor = matrix[j][i]
            if factor != 0:
                # Aplicar la eliminación
                matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(cols)]

        # Imprimir el estado de la matriz después de cada fila
        print(f"After processing row {i}:")
        for row in matrix:
            print(row)

    return matrix

# Ejecutar la función y mostrar la matriz resultante
result = gauss_matrix_solver(gauss_amplified_sample_matrix)
print("Final result:")
for row in result:
    print(row)
