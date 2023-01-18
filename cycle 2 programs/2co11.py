#write lamda function to find the area of square,rectangle and triangle
l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
h=int(input("Enter the height of triangle:"))
ar=lambda x,y:x*y
asq=lambda x:x*x
at=lambda x,y:0.5*x*y
print("Area of rectangle:",ar(l,b))
print("Area of square:",asq(l))
print("Area of triangle",at(b,h))