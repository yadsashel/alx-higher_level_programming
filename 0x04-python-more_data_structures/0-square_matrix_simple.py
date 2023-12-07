#!/urs/bin/python3

def square_matrix_simple(matrix=[]):
   
    new_matrix = []

    for row in matrix:

        squared_row = []

        for element in row:

            squared_row.append(elemet ** 2)

         new_matrix.append(squared_row)


        return new_matrix
