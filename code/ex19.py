

class Matrix:
    def __init__(self, n):
        self.size = n
        self.body = [[0 for r in range(0, n + 2)] for y in range(0, n + 2)]

        for i in range(0, self.size + 2):
            self.body[i][0] = -1
            self.body[i][self.size + 1] = -1
            self.body[0][i] = -1
            self.body[self.size + 1][i] = -1

        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.pos = (1, 1)
        self.dir = 0


    def __str__(self):
        mx = ''
        for r in range(0, self.size + 2):
            for c in range(0, self.size + 2):
                mx = mx + str(self.body[r][c]) + ' '
            mx += '\n'

        return mx

    def get(self, cell):
        return self.body[cell[0]][cell[1]]

    def set(self, cell, value):
        self.body[cell[0]][cell[1]] = value

    def step(self):
        d = self.dirs[self.dir]
        nx = (self.pos[0] + d[0], self.pos[1] + d[1])
        if self.body[nx[0]][nx[1]] != 0:
            self.dir = (self.dir + 1) % 4
            d = self.dirs[self.dir]
            nx = (self.pos[0] + d[0], self.pos[1] + d[1])
        self.pos = nx
            







if __name__ == '__main__':
    m = Matrix(5)
    print(m.pos)
    m.step()
    print(m.pos)
    m.step()
    print(m.pos)
    m.step()
    print(m.pos)
    m.step()
    print(m.pos)
    m.step()
    print(m.pos)

