from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#parse_file( 'script', edges, transform, screen, color )
#lol
add_edge(transform, 0, 0, 0, 100, 0, 0)
#lol
add_edge(transform, 100, 0, 0, 100, 100, 0)
#lol
add_edge(transform, 100, 100, 0, 0, 100, 0)
#lol
add_edge(transform, 0, 100, 0, 0, 0, 0)
#lol
add_edge(transform, 0, 0, 100, 100, 0, 100)
#lol
add_edge(transform, 100, 0, 100, 100, 100, 100)
#lol
add_edge(transform, 100, 100, 100, 0, 100, 100)
#lol
add_edge(transform, 0, 100, 100, 0, 0, 100)
#lol
add_edge(transform, 0, 0, 0, 0, 0, 100)
#lol
add_edge(transform, 0, 100, 0, 0, 100, 100)
#lol
add_edge(transform, 100, 100, 0, 100, 100, 100)
#lol
add_edge(transform, 100, 0, 0, 100, 0, 100)

make_scale(transform,2,2,2)

draw_lines( transform, screen, color )
display(screen)
