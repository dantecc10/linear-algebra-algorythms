import fractions_code as frc

def read_matrix(rows=False, columns=False):
    if rows == False:
        rows = int(input("Enter the number of rows: "))
    if columns == False:
        columns = int(input("Enter the number of columns: "))
    matrix = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(float(input("Enter the value of the matrix at index (" + str(i) + ", " + str(j) + "): ")))
        matrix.append(row)
        
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        row_str = ""
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                row_str += str(matrix[i][j])
            else:
                row_str += str(matrix[i][j]) + ", "
        print(row_str)
    print("")

def f_printer_matrix(matrix): # Imprime la matriz con fracciones en lugar de decimales y que se muestren las "esquinas de la matriz" para que no parezca un determinante
    print("┌")
    for i in range(len(matrix)):
        row_str = "|"
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                row_str += str(frc.fraction_val(matrix[i][j])) + "|"
            else:
                row_str += str(frc.fraction_val(matrix[i][j])) + " "
        print(row_str)
    print("└")
    