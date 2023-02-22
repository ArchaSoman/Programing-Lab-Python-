from graphics.rectangle import*
from graphics.circle import*
from graphics.threedgraphics.cuboid import*
from graphics.threedgraphics.sphere import*

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle:",rectarea(l,b))
print("Perimeter of rectangle:",rectperimeter(l,b))
r=int(input("Enter the radius:"))
print("Area of circle:",circlearea(r))
print("Perimeter of circle:",circleperimeter(r))
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
print("Area of cuboid:",cuboidarea(l,b,h))
print("Perimeter of cuboid",cuboidperimeter(l,b,h))
r=int(input("Enter the radius:"))
print("Area of sphere:",spherearea(r))
print("Perimeter of sphere",sphereperimeter(r))