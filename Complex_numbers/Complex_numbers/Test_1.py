from unittest import TestCase

class TestComplex(TestCase):
    def test_sumofcomplex(self):
        from Complex import Complex
        
        result = Complex(1,1) + Complex(2,2)
        self.assertTrue(result, Complex(3,3))
