from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import time

DELAY = 0.01

class Shape:
    def __init__(self):
        self.point_matrix = []
        self.point_matrix_old = []
        self.point_data = []
        self.num_of_point = 0

    def add_point(self, point):
        self.point_data = point.split(',')
        self.num_of_point = self.num_of_point + 1
        self.point_matrix.append([float(self.point_data[0]), float(self.point_data[1])])
        self.point_matrix_old.append([float(self.point_data[0]), float(self.point_data[1])])

    def _update_matrix(self, i):
        self.point_matrix_old[i][0] = self.point_matrix[i][0]
        self.point_matrix_old[i][1] = self.point_matrix[i][1]

    def animate(self, k):
        glClear(GL_COLOR_BUFFER_BIT)
        #drawGraph()
        glColor3f(33/255, 150/255, 243/255)
        glBegin(GL_POLYGON)
        tmp = []
        for j in range(self.num_of_point):
            dX = (self.point_matrix[j][0] - self.point_matrix_old[j][0])/100
            dY = (self.point_matrix[j][1] - self.point_matrix_old[j][1])/100
            tmp.append([self.point_matrix_old[j][0]+(k*dX), self.point_matrix_old[j][1]+(k*dY)])
        for j in tmp:
            glVertex2f(j[0]/500, j[1]/500)
        glEnd()
        glFlush()

    #@staticmethod
    def multiply_matrix(self,listA,listB):
        res = []
        for i in range(len(listA)):
            tmp = 0
            for j in range(len(listB)):
                tmp += listA[j][i] * listB[j]
                res.append(tmp)
        return res

    def translate(self, dx, dy):
        for i in range(self.num_of_point):
            self._update_matrix(i)
            self.point_matrix[i][0] += dx
            self.point_matrix[i][1] += dy
        for i in range(100):
            time.sleep(DELAY)
            self.animate(i)

    def dilate(self, zoom):
        for i in range(self.num_of_point):
            self._update_matrix(i)
            self.point_matrix[i][0] *= zoom
            self.point_matrix[i][1] *= zoom
        for i in range(100):
            time.sleep(DELAY)
            self.animate(i)

    def rotate(self, deg, x, y):
        matrix = []
        rad = math.radians(deg)
        matrix.append([float(math.cos(rad)), float(math.sin(rad))])
        matrix.append([float(math.sin(rad) * -1), float(math.cos(rad))])
        for i in range(self.num_of_point):
            self.point_matrix[i][0] -= x
            self.point_matrix[i][1] -= y
            res = self.multiply_matrix(matrix, self.point_matrix[i])
            self._update_matrix(i)
            self.point_matrix[i][0] = res[0] + x
            self.point_matrix[i][1] = res[1] + y
        for i in range(100):
            time.sleep(DELAY)
            self.animate(i)

    def reflect(self, param):
        if param == 'x':
            for i in range(self.num_of_point):
                self._update_matrix(i)
                self.point_matrix[i][1] *= -1
        elif param == 'y':
            for i in range(self.num_of_point):
                self._update_matrix(i)
                self.point_matrix[i][0] *= -1
        elif param == 'y=x':
            for i in range(self.num_of_point):
                self._update_matrix(i)
                self.point_matrix[i][0], self.point_matrix[i][1] = self.point_matrix[i][1], self.point_matrix[i][0]
        elif param == 'y=-x':
            for i in range(self.num_of_point):
                self._update_matrix(i)
                self.point_matrix[i][0], self.point_matrix[i][1] = self.point_matrix[i][1], self.point_matrix[i][0]
                self.point_matrix[i][1] *= -1
                self.point_matrix[i][0] *= -1
        else :
            for i in range(self.num_of_point):
                self._update_matrix(i)
                self.point_matrix[i][0] = 2*float(param[1]) - self.point_matrix[i][0]
                self.point_matrix[i][1] = 2*float(param[3]) - self.point_matrix[i][1]
        for i in range(100):
            time.sleep(DELAY)
            self.animate(i)

    def print_point(self):
        for x in self.point_matrix:
            print(x[0], ' ', x[1])

    def print_point_old(self):
        for x in self.point_matrix_old:
            print(x[0], ' ', x[1])

    def get_point(self):
        return self.point_matrix

    def get_old_point(self):
        return self.point_matrix_old
