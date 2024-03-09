from shapelib import api
from shapelib.core.shapes import _Shape, _Circle, _Triangle
print(api.calculate_circle_area_by_radius(10)) #314.15000000000003
print(api.calculate_triangle_area_by_tree_sides(3, 4, 6)) #5.332682251925386
print(api.is_rectangular_by_three_sides(3, 4, 6)) #False
 


def make_area_calculating_with_shape(shape: _Shape):
    return shape.calculate_area()

print('-'*50)
for shape in [_Circle(43), _Triangle(4, 5, 6), _Triangle(12, 4, 10)]:
    print(make_area_calculating_with_shape(shape))