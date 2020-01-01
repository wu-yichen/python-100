import sys
import unittest


class Question5:

    input = ''

    def getString(self, input):
        self.input = input

    def printString(self):
        print(self.input.upper())


if __name__ == '__main__':
    input = sys.argv[1]
    q5 = Question5()
    q5.getString(input)
    q5.printString()
