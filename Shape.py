

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

    def translate(self, dx, dy):
        for i in range(self.num_of_point):
            self._update_matrix(i)
            self.point_matrix[i][0] += dx
            self.point_matrix[i][1] += dy

    def dilate(self, zoom):
        for i in range(self.num_of_point):
            self._update_matrix(i)
            self.point_matrix[i][0] *= zoom
            self.point_matrix[i][1] *= zoom

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
