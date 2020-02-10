
import unittest
import delaunay

class TestDelaunay(unittest.TestCase):

    def test_sequence(self):
        params = [
            (2,0, [0,1]),
            (4,0, [0,1,0,1]),
            (4,1, [0,0,1,1])
        ]
        for (n,d,s) in params:
            assertSequenceEqual(list(delaunay.sequence(n,d)), s )



if __name__ == '__main__':
    unittest.main()