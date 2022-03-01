
#Elizabeth Montero
#02/1/22

#Problem 1 writing a function areaOfCircle that retunrs to the area and prints
#Problem1Area of circle
import math

def area_of_circle(r):

    area_of_circle = r * r * math.pi
    return area_of_circle

r = 10 # the result of the circle
result = area_of_circle 
print ("The area of the circle is", result)

#Problem 2 a python function that checks a number in a given range
#Problem 2 Check Range

def test_range(n):
    if n in range(3,9): # the range it is choosing from
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

#Problem 3 function that multiplys all the numbers on the list
#Problem3Multilply
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply((5, 2, 7, 7, -1))) # multiplying all numbers

#Problem 4 A python function that takes a list and retunrs new list with unique elements
#Problem4Unique

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))

#Problem 5 a chunk code as a base to produce the image
#Problem5Squares

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawSquares(number_of_squares, square_size):
    for count in range(number_of_squares):
        drawSquare(alex, square_size)
        alex.penup()
        alex.left(180)
        alex.forward(10)
        alex.left(90)
        alex.forward(10)
        alex.left(90)
        alex.pendown()
        square_size = square_size + 20

drawSquares(2, 20)

wn.exitonclick()


#Problem  6
#Problem6Flower
import turtle
  
t = turtle.Turtle()
  
# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))
  
# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))
  
  
for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
