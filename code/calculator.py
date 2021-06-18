

class Calculator:
    FUNCS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    def __init__(self):
        self.accumulator = 0
        self.screen = '0'
        self.operation = ''


    def write(self, sym):
        if sym in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.screen += sym
        elif sym in ['+', '-', '*', '/']:
            if self.screen != '0':
                if self.operation == '':
                    self.operation = sym
                    self.accumulator = float(self.screen)
                    self.screen = ''
                else:
                    self.accumulator = self.funcs[self.operation](self.accumulator, float(self.screen))
                    self.operation = sym
        elif sym == '=':
            pass
        elif sym == 'C':
            self.accumulator = 0
            self.screen = '0'
            self.operation = ''






if __name__ == '__main__':
    calc = Calculator()

