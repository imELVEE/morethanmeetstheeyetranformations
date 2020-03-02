from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname,'r')
    commands = file.readlines()
    i = 0
    while i < len(commands):
        if commands[i] == 'line\n':
            p = commands[i+1].split(' ')
            add_edge(points,int(p[0]),int(p[1]),int(p[2]),int(p[3]),int(p[4]),int(p[5]))

        if commands[i] == 'ident\n':
            ident(transform)

        if commands[i] == 'scale\n':
            p = commands[i+1].split(' ')
            make_scale(transform,int(p[0]),int(p[1]),int(p[2]))

        if commands[i] == 'move\n':
            p = commands[i+1].split(' ')
            make_translate(transform,int(p[0]),int(p[1]),int(p[2]))

        if commands[i] == 'rotate\n':
            p = commands[i+1].split(' ')
            if p[0] == 'x':
                make_rotX(transform,int(p[1]))
            if p[0] == 'y':
                make_rotY(transform,int(p[1]))
            if p[0] == 'z':
                make_rotZ(transform,int(p[1]))

        if commands[i] == 'apply\n':
            matrix_mult(transform,points)
            for r in range(len(points)):
                for c in range(len(points[r])):
                    points[r][c] = int(points[r][c])

        if commands[i] == 'display\n':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        if commands[i] == "save\n":
            p = commands[i+1]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_ppm(screen, p[:-1])

        if commands[i] == 'quit\n':
            break

        i += 1
