import numpy as np

class Demo():
    def __init__(self, str1):
        self.str1 = str1

    def print_string(self):
        print(self.str1)
        return 0

char = Demo("It's demo.")
char.print_string()