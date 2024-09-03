# Part 1 A -- Make a Line
def make_line(size):
    line = ''
    for i in range(size):
        line += '#'
    return line

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(side):
    for i in range(side):
        print(make_line(side))





# Part 1 C -- Make a Rectangle
def make_rectangle(side_a,side_b):
    for i in range(side_a):
        print(make_line(side_b))

make_rectangle(3,7)


# Part 2 A -- Make a Stairs





# Part 2 B -- Make Space-Line 





# Part 2 C -- Make Isosceles Triangle





# Part 3 -- Make a Diamond






