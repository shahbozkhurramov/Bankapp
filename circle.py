from point import Point
class Circle:
  def __init__(self,x,y,radius:int):
    self.markaz=Point(x,y)
    self.radius=radius
  def isinside(self,x1,y1):
    if self.markaz.distance(x1,y1)<=self.radius:
      return True
      # if distance between one point and the center of circle is 
      # less than radius it means that the point is inside the circle
    #   in this case we return true 
    # else false
    else: 
      return False