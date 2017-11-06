from Shape import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time


DEBUG = True

shape = Shape()
SCALE = 500
FPS = 100
RATE = 1


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def input_matrix():
    global shape
    print('Enter the number of point: ')
    number_of_points = int(input())
    for i in range(number_of_points):
        shape.add_point(input())

    glutDisplayFunc(draw_plane)


def animate():
    for i in range(FPS):
        time.sleep(DELAY)
        global shape
        glClear(GL_COLOR_BUFFER_BIT)
        draw_graph()
        glColor3f(33/255, 150/255, 243/255)
        glBegin(GL_POLYGON)
        tmp = []
        for j in range(shape.num_of_point):
            d_x = (shape.point_matrix[j][0] - shape.point_matrix_old[j][0])/100
            d_y = (shape.point_matrix[j][1] - shape.point_matrix_old[j][1])/100
            tmp.append([shape.point_matrix_old[j][0]+(i * d_x), shape.point_matrix_old[j][1]+(i * d_y)])
        for j in tmp:
            glVertex2f(j[0]/500, j[1]/500)
        glEnd()
        glFlush()


def animate_rotate(deg):
    for i in range(100):
        time.sleep(DELAY)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(33/255, 150/255, 243/255)
        glBegin(GL_POLYGON)
        deg /= 100
        tmp = []
        for j in range(shape.num_of_point):
            d_x = (shape.point_matrix[j][0] - shape.point_matrix_old[j][0])/100
            d_y = (shape.point_matrix[j][1] - shape.point_matrix_old[j][1])/100
            tmp.append([shape.point_matrix_old[j][0]+(i*d_x), shape.point_matrix_old[j][1]+(i*d_y)])
        for j in tmp:
            glVertex2f(j[0]/500, j[1]/500)
        glEnd()
        glFlush()


def parse_task(input_parse):
    keyword = input_parse[0]

    global shape

    if keyword == 'translate':
        dx = float(input_parse[1])
        dy = float(input_parse[2])
        shape.translate(dx, dy)
    elif keyword == 'dilate':
        zoom = float(input_parse[1])
        shape.dilate(zoom)
    elif keyword == 'rotate':
        deg = float(input_parse[1])
        x = float(input_parse[2])
        y = float(input_parse[3])
        shape.rotate(deg, x, y)
    elif keyword == 'reflect':
        param = input_parse[1]
        shape.reflect(param)
    elif keyword == 'shear':
        axis = input_parse[1]
        coefficient = input_parse[2]
        shape.shear(axis, float(coefficient))
    elif keyword == 'stretch':
        axis = input_parse[1]
        coefficient = input_parse[2]
        shape.stretch(axis, float(coefficient))
    elif keyword == 'custom':
        a = input_parse[1]
        b = input_parse[2]
        c = input_parse[3]
        d = input_parse[4]
        custom = [[float(a), float(b)], [float(c), float(d)]]
        shape.custom(custom)


def main_menu():
    print('Enter a task: ')
    input_parse = input().split()
    keyword = input_parse[0]

    global shape

    if keyword == 'input':
        input_matrix()
    elif keyword == 'reset':
        shape.reset()
        animate()
    elif keyword == 'multiple':
        n = int(input_parse[1])
        for i in range(n):
            multi_input = input().split()
            parse_task(multi_input)
        animate()
    elif keyword == 'exit':
        glutLeaveMainLoop()
    else:
        parse_task(input_parse)
        animate()

    glutPostRedisplay()


def draw_graph():
    global SCALE
    glColor3f(206/255, 206/255, 206/255)
    glLineWidth(0.01)
    glBegin(GL_LINES)
    for i in range(-int((SCALE / 20 + 1)), int(SCALE / 20)):
        glVertex2f(i/int(SCALE / 20), 1.0)
        glVertex2f(i/int(SCALE / 20), -1.0)
        glVertex2f(1.0, i/int(SCALE / 20))
        glVertex2f(-1.0, i/int(SCALE / 20))
    glEnd()

    glColor3f(130/255, 130/255, 130/255)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex2f(0.0, 1.0)
    glVertex2f(0.0, -1.0)
    glVertex2f(1.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glEnd()


def cartesian():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    draw_graph()
    glFlush()


def draw_plane():
    global shape, SCALE

    glClear(GL_COLOR_BUFFER_BIT)
    draw_graph()

    point_matrix = shape.get_point()
    point_matrix_old = shape.get_old_point()

    glColor3f(144/255, 202/255, 249/255)
    glBegin(GL_POLYGON)
    for x in point_matrix_old:
        glVertex2f(x[0]/SCALE, x[1]/SCALE)
    glEnd()

    glColor3f(33/255, 150/255, 243/255)
    glBegin(GL_POLYGON)
    for x in point_matrix:
        glVertex2f(x[0]/SCALE, x[1]/SCALE)
    glEnd()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow('Ayy LMAO')
    glutDisplayFunc(draw_plane)
    glutIdleFunc(main_menu)
    init()
    glutMainLoop()


main()
