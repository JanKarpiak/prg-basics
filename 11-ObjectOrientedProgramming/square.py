class Square():
      def __init__(self, a):
        self.a = a
      def area(self):
        return self.a * self.a
    

square1 = Square(4)
square2 = Square(6)

print(f'Square with side 4: {square1.a} ')
print(f'Area is {square1.area}, Perimeter is {square1.a * 4}')
print (f'Square with side 6: {square2.a}')