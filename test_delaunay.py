
import unittest
import delaunay
import numpy as np
class TestDelaunay(unittest.TestCase):

    def generate_points(self, N,D):
        for _p in np.random.rand(N,D):
            yield tuple(_p)
        
    def test_delaunay_init_infer_D(self):
        N = 5
        D = 2
        P = list(self.generate_points(N,D))
        _delaunay = delaunay.Delaunay(P)

        # infer D from P if no D arg
        self.assertEquals(_delaunay.D, D, msg="infer D from P if no D arg")
        
    def test_delaunay_init_D_eq_dimP(self):
        N = 5
        D = 2
        P = list(self.generate_points(N,D))
        
        # if provided D should be same order as P, if not throw exception
        self.assertRaises(Exception, delaunay.Delaunay, P, D+1 )
        _delaunay = delaunay.Delaunay(P,D)
    
    def test_delaunay_init_D_gteq_2(self):
        N = 5
        D = 1
        P = list(self.generate_points(N,D))
        
        # if provided D should be same order as P, if not throw exception
        self.assertRaises(Exception, delaunay.Delaunay, P, D )
        

    def test_box(self):
        return
        #_delaunay = delaunay.Delaunay(P)

    def test_sequence(self):
        params = [
            (2,0, [0,1]),
            (4,0, [0,1,0,1]),
            (4,1, [0,0,1,1]),
            (8,0, [0,1,0,1,0,1,0,1]),
            (8,1, [0,0,1,1,0,0,1,1]),
            (8,2, [0,0,0,0,1,1,1,1]),
            (16,0, [0,1,0,1,0,1,0,1, 0,1,0,1,0,1,0,1]),
            (16,1, [0,0,1,1,0,0,1,1, 0,0,1,1,0,0,1,1]),
            (16,2, [0,0,0,0,1,1,1,1, 0,0,0,0,1,1,1,1]),
            (16,3, [0,0,0,0,0,0,0,0, 1,1,1,1,1,1,1,1])
        ]
        for (n,d,s) in params:
            #print("{0} {1} {2} {3}".format(n,d,s, list(delaunay.sequence(n,d))))

            self.assertSequenceEqual(list(delaunay.sequence(n,d)), s)



if __name__ == '__main__':
    unittest.main()