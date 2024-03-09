import unittest

from shapelib import api
from shapelib.core.exceptions import ShapeParamsError

class TestShapeApi(unittest.TestCase):
    def setUp(self):
        #init_something()
        pass
        
    def tearDown(self):
        #teardown_something()
        pass
        
    def test_circle_area(self):
        self.assertEqual(api.calculate_circle_area_by_radius(10), 314.15000000000003)
    
    def test_triangle_area(self):
        self.assertEqual(api.calculate_triangle_area_by_tree_sides(3, 4, 6), 5.332682251925386)

    def test_triangle_no_rectangular(self):
        self.assertEqual(api.is_rectangular_by_three_sides(3, 4, 6), False)
    
    def test_triangle_incorrect_params(self):
        with self.assertRaises(ShapeParamsError):
            api.is_rectangular_by_three_sides(-3, 4, 6)

    def test_circle_incorrect_params(self):
        with self.assertRaises(ShapeParamsError):
            api.calculate_circle_area_by_radius(-3)
            
    def test_triangle_rectangular(self):
        self.assertEqual(api.is_rectangular_by_three_sides(3, 4, 5), True)

        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShapeApi)
    unittest.TextTestRunner(verbosity=2).run(suite)