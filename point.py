from math import sqrt
class Point:
  def __init__(self, x:int,y:int):
    self.x=x
    self.y=y
  def distance(self,x1,y1):
    return sqrt((x1-self.x)**2+(y1-self.y)**2)
    # distance beetwen 2 coordinates can be found by 
    # adding the square of two points' difference(x1,x2 and y1,y2) and 
    # taking the square root of their sum