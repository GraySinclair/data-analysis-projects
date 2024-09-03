# Part 1 A -- Make a Line
def make_line(size = 9):
    line = ''
    for i in range(size):
        line += '#'
    return line

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
def make_square(side = 3):
    for i in range(side):
        print(make_line(side))





# Part 1 C -- Make a Rectangle
def make_rectangle(side_a = 2,side_b = 3):
    for i in range(side_a):
        print(make_line(side_b))


# Part 2 A -- Make a Stairs
def make_stairs(step_num = 9):
    for i in range(step_num):
        print(make_line(i+1))



# Part 2 B -- Make Space-Line 
def make_space_line(numspaces = 3, numchara = 3):
    spaceline = ''
    for i in range(numspaces):
        spaceline += '_'
    for i in range(numchara):
        spaceline += '#'
    for i in range(numspaces):
        spaceline += '_'
    print(spaceline)



# Part 2 C -- Make Isosceles Triangle
def make_triangle(height = 6):
   triangle = ""
   for i in range(height):
        while i > height:
            if triangle % 2 == 0:
                triangle += '#'
            else:
                triangle += '##'
            print(triangle)

make_triangle()

# Part 3 -- Make a Diamond






