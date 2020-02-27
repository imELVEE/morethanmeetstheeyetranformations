from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 182, 193 ]
matrix = new_matrix(0,0)

#lol
add_edge(matrix, 0, 0, 0, 100, 0, 0)
#lol
add_edge(matrix, 100, 0, 0, 100, 100, 0)
#lol
add_edge(matrix, 100, 100, 0, 0, 100, 0)
#lol
add_edge(matrix, 0, 100, 0, 0, 0, 0)
#lol
add_edge(matrix, 0, 0, 100, 100, 0, 100)
#lol
add_edge(matrix, 100, 0, 100, 100, 100, 100)
#lol
add_edge(matrix, 100, 100, 100, 0, 100, 100)
#lol
add_edge(matrix, 0, 100, 100, 0, 0, 100)
#lol
add_edge(matrix, 0, 0, 0, 0, 0, 100)
#lol
add_edge(matrix, 0, 100, 0, 0, 100, 100)
#lol
add_edge(matrix, 100, 100, 0, 100, 100, 100)
#lol
add_edge(matrix, 100, 0, 0, 100, 0, 100)

draw_lines( matrix, screen, color )
display(screen)
