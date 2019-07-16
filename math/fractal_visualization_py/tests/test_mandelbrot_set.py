import unittest

from .context import fractal_visualization_py as fv

class TestMandelbrotSet(unittest.TestCase):
    def test_mandelbrot_function(self):
        expected = 1j
        actual = fv.mandelbrot_set.mandelbrot_function(0, 1j)
        self.assertEqual(actual, expected)
