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

def make_space_line(numSpaces, numChars):
    line = ' ' * numSpaces + '#' * numChars + ' ' * numSpaces
    return line


# Part 2 C -- Make Isosceles Triangle
def make_isosceles_triangle(height):
   triangle = ''
   for i in range(height):
      triangle += (make_space_line(height - i - 1, 2 * i + 1) + '\n')
   return triangle


# Part 3 -- Make a Diamond
def make_diamond(height):
   diamond = ''
   triangle = make_isosceles_triangle(height)
   diamond += triangle[:-1]
   for i in range(len(triangle)-1, -1, -1):
      diamond += triangle[i]
   return diamond

print(make_diamond(5))
