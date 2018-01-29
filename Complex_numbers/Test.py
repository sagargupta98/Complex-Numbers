from __future__ import division
from unittest import TestCase
from Complex import Complex


class TestComplex(TestCase): 
    def test_sumofcomplex(self):
        result = Complex(1,2).real + Complex(2,3).real
        self.assertEqual(result, Complex(3,5).real)
        
    def test_diffofcomplex(self):
        result = Complex(1,2) - Complex(2,3)
        self.assertEqual(result, Complex(-1,-1))
        
    def test_productofcomplex(self):
        result = Complex(1,2) * Complex(2,3)
        self.assertEqual(result, Complex(-4,7))
        
    def test_conjugateofcomplex(self):
        result = Complex(1,2).conjugate()
        self.assertEqual(result, Complex(1,-2))
        
    def test_absoluteofcomplex(self):
        result = Complex(1,2).abs()
        self.assertEqual(result, 2.23606797749979)
        
    def test_powerofcomplex(self):
        result = Complex(1,2)**3
        self.assertEqual(result, Complex(-527,336))
        
    def test_divisionofcomplex(self):
        result = Complex(2,3) / (Complex(1,2))
        self.assertEqual(result, Complex(1.5999999999999996,-0.19999999999999996))
        
    def test_anglerofcomplex(self):
        result = Complex(1,2).angle()
        self.assertEqual(result, 26.56505117707799)
    
    def test_polarformofcomplex(self):
        result = Complex(1,2).polarform()
        self.assertEqual(result, '2.2360679775(cos(26.5650511771) + sin(26.5650511771)i)')



