"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    m = ""
    for i in range(4):
        for v in matrix[i]:
            m += str(v) + " "
        m += "\n"
    print(m)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    return [[1.0 , 0.0 , 0.0 , 0.0],
            [0.0 , 1.0 , 0.0 , 0.0],
            [0.0 , 0.0 , 1.0 , 0.0],
            [0.0 , 0.0 , 0.0 , 1.0],
                                    ]

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #make answer the correct size
    answer = []
    for r in range(len(m1)):
        answer.append([])
        for c in m2[0]:
            answer[r].append(0)

#    for row in m1:
#        for col in m2:
#            answer[row][col] = dot product

#do it by index, not with for, so while loop
    row = 0
    while row < len(m1):
        col = 0
        while col < len(m2[0]):
            answer[row][col] = dot_product(m1,m2,row,col)
            col += 1
        row += 1

    #m2 becomes the new matrix
    row = 0
    while row < len(m2):
        col = 0
        while col < len(m2[row]):
            m2[row][col] = answer[row][col]
            col += 1
        row += 1


def dot_product(m1,m2,r,c):
    sum = 0
    for i in range(len(m1)):
        sum += m1[r][i] * m2[i][c]
    return sum


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
