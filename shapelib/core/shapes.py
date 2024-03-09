from abc import ABC, ABCMeta, abstractclassmethod
from shapelib.core.exceptions import ShapeParamsError


class _Shape(ABC):
    __metaclass__=ABCMeta

    @abstractclassmethod
    def calculate_area(self):
        ''' it returns an area of any shape object '''
        pass

    @abstractclassmethod
    def _validate_shape(self, *args, **kwargs) -> bool:
        ''' It validates the shape based on the provided initialization parameters. '''
        pass



class _Circle(_Shape):
    PI = 3.1415
    def __init__(self, radius):
        self._validate_shape(radius)
        self.radius = radius
    
    def calculate_area(self):
        area = self.PI * (self.radius ** 2)
        return area
    
    def _validate_shape(self, radius):
        if radius <= 0:
            raise ShapeParamsError('Отрицательного радиуса окружности быть не может!')
    

class _Triangle(_Shape):
    def __init__(self, side1, side2, side3 ):
        self._validate_shape(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        

    def calculate_area(self):
        semi_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = (semi_perimeter*(semi_perimeter-self.side1)*(semi_perimeter-self.side2)*(semi_perimeter-self.side3)) ** 0.5
        return area
    
    def _validate_shape(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ShapeParamsError('Отрицательных сторон треугольника быть не может!')
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side3 + side2 <= side1):
            raise ShapeParamsError('Не выполняется условие системы неравенств сторон треугольника!')
        
    def is_rectangular(self):
        ''' checking if triangle is right '''
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0]**2 + sides[1]**2 == sides[2]**2
            