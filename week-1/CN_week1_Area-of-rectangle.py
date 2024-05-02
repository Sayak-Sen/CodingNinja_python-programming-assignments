"""
You are given a rectangle in a plane whose sides are parallel to the axes.
The coordinates of one of its diagonals are provided to you.
You have to print the total area of the rectangle.

The coordinates of the rectangle are provided as four integral values: x1, y1, x2, y2.
It is given that x1 < x2 and y1 < y2.

"""
x1=int(input("x1= "))
y1=int(input("y1= "))
x2=int(input("x2= "))
y2=int(input("y2= "))
#horizontal length of rectangle is abs(x2-x1)
horizontal_length=abs(x2-x1)
#vertical length of rectangle is abs(y2-y1)
varticle_length=abs(y2-y1)
area=horizontal_length*varticle_length
print("area of the rectangle is %i"%area)
