from circle import Circle
class Prince:
  def __init__(self,x1,y1,x2,y2):
    self.x1=x1
    self.y1=y1
    self.x2=x2
    self.y2=y2
  def cross(self,x,y,r):
    self.aylana1=Circle(x,y,r)
    if self.aylana1.isinside(self.x1,self.y1)==self.aylana1.isinside(self.x2,self.y2):
      return False
      # if prince and princess are both inside the circle prince does not cross through the circle 
    else: return True
    # if one of them inside the circle and other one is not inside prince crosses the circle