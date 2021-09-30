from prince import Prince
t=int(input())
#testcase input
for i in range(t):
  x1,y1,x2,y2=map(int, input().split())
    # points of prince and princess
  prince=Prince(x1,y1,x2,y2)
  # everything is clear here 
  n=int(input())
  count=0
  for j in range(n):
    cx,cy,r=map(int, input().split())
    if prince.cross(cx,cy,r):
      # if prince crosses the planet function returs true and 
      # count is increased by one else nothing is executed
      count+=1
  print(count)