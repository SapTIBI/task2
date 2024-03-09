from shapelib.core.shapes import _Circle, _Triangle

def calculate_circle_area_by_radius(radius) -> float:
    return _Circle(radius=radius).calculate_area()

def calculate_triangle_area_by_tree_sides(side1, side2, side3) -> float:
    return _Triangle(side1, side2, side3).calculate_area()

def is_rectangular_by_three_sides(side1, side2, side3) -> bool:
    return _Triangle(side1, side2, side3).is_rectangular()

