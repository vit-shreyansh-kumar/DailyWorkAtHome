__about__ = """Flatten the nested matrix"""

matrix = [[1,2,3,4,5,6],[7,8,9,10],[11,12,1,13,14,15,16]]

""" Flattening the matrix. """

matrix_flat = [ x for row in matrix for x in row ]

print("The flat Matrix is:", matrix_flat)

new_matrix = [[1,2,3,4,55],[6,7,8,9,10],[11,12,13,14,15,16,17]]

""" Flatten the new matrix. """

new_matrix_flatten = [ x for row in new_matrix for x in row]

print(new_matrix_flatten)