class Point2D:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    # # Implements addition so we can do point1 + point2
    # # self refers to the left hand operand (point1)
    # # other refers to the right-hand operand (point2)
    # def __add__(self: Point2D, other: Point2D) -> Point2D:
    #     if isinstance(other, Point2D):
    #         x_sum = self.__x + other.__x
    #         y_sum = self.__y + other.__y

    #         return Point2D(x_sum, y_sum)
        
    #     return NotImplemented
    
    # def __sub__(self: Point2D, other: Point2D) -> Point2D:
    #     if isinstance(other, Point2D):
    #         x_diff = self.__x - other.__x
    #         y_diff = self.__y - other.__y

    #         return Point2D(x_diff, y_diff)
        
    #     return NotImplemented
    
    # # For two points we will compute the Dot Product
    # # If self and other are both Point2D objects
    # #   compute the dot product: (x1, y1) * (x2, y2) = x1 * x2 + y1 * y2
    # # If self or other is a Scalar:
    # #   compute Scalar Multiplication: 2 * (x, y) = (2x, 2y)
    # def __mul__(self: Point2D, other: Point2D) -> (float | Point2D):
    #     if isinstance(other, Point2D):
    #         x_prod = self.__x * other.__x
    #         y_prod = self.__y * other.__y

    #         return x_prod * y_prod

    #     elif isinstance(other, (int, float)):
    #         return Point2D(self.__x * other, self.__y * other)
        
    #     return NotImplemented

    # def __rmul__(self: Point2D, other: (int | float)) -> Point2D:
    #     if isinstance(other, (int, float)):
    #         return Point2D(self.__x * other, self.__y * other)
        
    #     return NotImplemented
    
    # def __iadd__(self: Point2D, other: Point2D) -> Point2D:
    #     if isinstance(other, Point2D):
    #         self.__x += other.__x
    #         self.__y += other.__y
    #         return self
        
    #     return NotImplemented

    # def __neg__(self: Point2D) -> Point2D:
    #     # We do not need to check isinstance() since self will always be
    #     # a Point2D object in this class.

    #     # __neg__ should be designed to not change the original value.
    #     # return a new object with the changes.
    #     return Point2D(-self.__x, -self.__y)
              
    # def __eq__(self: Point2D, other: Point2D) -> Point2D:
    #     if isinstance(other, Point2D):
    #         return self.__x == other.__x and self.__y == other.__y

    #     return NotImplemented

    # def __getitem__(self, index):
    #     if index == 0:
    #         return self.__x
    #     elif index == 1:
    #         return self.__y
    #     else:
    #         raise IndexError("Point2D index out of range")


    
    # def __setitem__(self, index, value):
    #     if index == 0:
    #         self.x = value
    #     elif index == 1:
    #         self.y = value
    #     else:
    #         raise IndexError("Point2D index out of range")

    # # Return a string in the format (x, y)
    # def __str__(self) -> str:
    #     return f'({self.__x}, {self.__y})'
    
    # def __repr__(self) -> str:
    #     # Point2D(3, 7)
    #     return f'Point2D(x={self.__x}, y={self.__y})'