class Rectangle:
    def __init__(self):
        self.__l=int(input("Length:"))
        self.__b=int(input("Breadth:"))
        
    def __lt__(self,ob2):
        area1=self.__l*self.__b
        area2=ob2.__l*ob2.__b
        print("Area of Rectangle 1 is",area1)
        print("Area of Rectangle 2 is",area2)
        return True
print("Enter the length and breadth of first object")
ob1=Rectangle()
print("Enter the length and breadth of second object")
ob2=Rectangle()
if ob1<ob2:
    print("Rectangle 1 is less than Rectangle 2")
else:
    print("Rectangle 1 is greater than Rectangle 2")
    
