from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(0,0)

add_edge(matrix,245,190,0,255,190,0)
add_edge(matrix,235,200,0,245,190,0)
add_edge(matrix,265,200,0,255,190,0)
add_edge(matrix,225,215,0,235,200,0)
add_edge(matrix,275,215,0,265,200,0)

add_edge(matrix,210,260,0,225,215,0)
add_edge(matrix,290,260,0,275,215,0)

add_edge(matrix,215,275,0,210,260,0)
add_edge(matrix,285,275,0,290,260,0)

add_edge(matrix,235,250,0,215,275,0)
add_edge(matrix,265,250,0,285,275,0)

add_edge(matrix,250,258,0,235,250,0)
add_edge(matrix,250,258,0,265,250,0)

'''
matrix2 = new_matrix()

identi = ident(matrix)
matrix = [[1.00, 4.00, 7.00, 10.00],
          [2.00, 5.00, 8.00, 11.00],
          [3.00, 6.00, 9.00, 12.00],
          [1.00, 1.00, 1.00, 1.00]]
matrix2 = [[1.00, 4.00],
           [2.00, 5.00],
           [3.00, 6.00],
           [1.00, 1.00]]

print_matrix(matrix)
print_matrix(matrix2)
matrix_mult(matrix,matrix2)
print_matrix(matrix2)
print_matrix(identi)
'''

draw_lines( matrix, screen, color )
display(screen)
