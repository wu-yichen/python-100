import sys
import unittest
from unittest.mock import patch
from question5 import Question5
import io


class Question5Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q5 = Question5()

    def testGetString(self):
        self.q5.getString('test')
        self.assertEqual(self.q5.input, 'test')

    @patch('sys.stdout', new_callable=io.StringIO)
    def testPrintString(self, mock_stdout):
        self.q5.printString()
        self.assertEqual(mock_stdout.getvalue(), 'TEST\n')


if __name__ == '__main__':
    unittest.main()
