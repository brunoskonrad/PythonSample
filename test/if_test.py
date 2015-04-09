import unittest
from sample import if_sample

class IfTestCase(unittest.TestCase):

    def test_basic(self):
        m = if_sample.basic(20)
        self.assertEqual(m, 'Sucesso, gente')


if __name__ == '__main__':
    unittest.main()
