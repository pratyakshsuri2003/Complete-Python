class Area:
    def find_area(self, x=None, y=None):
        if x!=None and y!=None:
            print("Area of ractangle: ", x*y)
        elif x!=None:
            print("Area of Square: ", x*x)
        else:
            print("Nothing is passed to claculate the area !!")

obj1 = Area()
obj1.find_area()
obj1.find_area(5)
obj1.find_area(12, 5)