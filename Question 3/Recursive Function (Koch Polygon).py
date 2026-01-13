
import turtle

def koch_inward(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3.0

        koch_inward(t, order - 1, size)
        t.left(60)
        koch_inward(t, order - 1, size)
        t.right(120)
        koch_inward(t, order - 1, size)
        t.left(60)
        koch_inward(t, order - 1, size)

def draw_inward_koch_polygon(sides, order, size):

    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    t = turtle.Turtle()
    t.speed(0)

    angle = 360 / sides

    for _ in range(sides):
        koch_inward(t, order, size)
        t.left(angle)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":

    sides = int(input("Enter number of sides: "))
    SIDE_LENGTH = int(input("Enter side length: "))
    depth = int(input("Enter the recursion depth: "))

    draw_inward_koch_polygon(sides, depth, SIDE_LENGTH)

