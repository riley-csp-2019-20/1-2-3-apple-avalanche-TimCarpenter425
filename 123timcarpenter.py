#   a123_apple_1.py
import turtle as trtl
import random as rndm

apple_image = "apple.gif" # Store the file name of your shape

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width = 1.0, height = 1.0)
wn.bgpic("tree.gif")

apple = trtl.Turtle()
apple.penup()
apple.speed(0)

letter = trtl.Turtle()
letter.ht()
letter.speed(0)
letter.penup()
letter.pencolor("white")

# given a turtle, set that turtle to be shaped by the image file
def start_gravity_a():
    global g
    global new_letter
    if(new_letter == "A"):
        g = 1
        gravity()
def start_gravity_b():
    global g
    global new_letter
    if(new_letter == "B"):
        g = 1
        gravity()
def start_gravity_c():
    global g
    global new_letter
    if(new_letter == "C"):
        g = 1
        gravity()
def start_gravity_d():
    global g
    global new_letter
    if(new_letter == "D"):
        g = 1
        gravity()
def start_gravity_e():
    global g
    global new_letter
    if(new_letter == "E"):
        g = 1
        gravity()
def start_gravity_f():
    global g
    global new_letter
    if(new_letter == "F"):
        g = 1
        gravity()
def start_gravity_g():
    global g
    global new_letter
    if(new_letter == "G"):
        g = 1
        gravity()
def start_gravity_h():
    global g
    global new_letter
    if(new_letter == "H"):
        g = 1
        gravity()
def start_gravity_i():
    global g
    global new_letter
    if(new_letter == "I"):
        g = 1
        gravity()
def start_gravity_j():
    global g
    global new_letter
    if(new_letter == "J"):
        g = 1
        gravity()
def start_gravity_k():
    global g
    global new_letter
    if(new_letter == "K"):
        g = 1
        gravity()
def start_gravity_l():
    global g
    global new_letter
    if(new_letter == "L"):
        g = 1
        gravity()
def start_gravity_m():
    global g
    global new_letter
    if(new_letter == "M"):
        g = 1
        gravity()
def start_gravity_n():
    global g
    global new_letter
    if(new_letter == "N"):
        g = 1
        gravity()
def start_gravity_o():
    global g
    global new_letter
    if(new_letter == "O"):
        g = 1
        gravity()
def start_gravity_p():
    global g
    global new_letter
    if(new_letter == "P"):
        g = 1
        gravity()
def start_gravity_q():
    global g
    global new_letter
    if(new_letter == "Q"):
        g = 1
        gravity()
def start_gravity_r():
    global g
    global new_letter
    if(new_letter == "R"):
        g = 1
        gravity()
def start_gravity_s():
    global g
    global new_letter
    if(new_letter == "S"):
        g = 1
        gravity()
def start_gravity_t():
    global g
    global new_letter
    if(new_letter == "T"):
        g = 1
        gravity()
def start_gravity_u():
    global g
    global new_letter
    if(new_letter == "U"):
        g = 1
        gravity()
def start_gravity_v():
    global g
    global new_letter
    if(new_letter == "V"):
        g = 1
        gravity()
def start_gravity_w():
    global g
    global new_letter
    if(new_letter == "W"):
        g = 1
        gravity()
def start_gravity_x():
    global g
    global new_letter
    if(new_letter == "X"):
        g = 1
        gravity()
def start_gravity_y():
    global g
    global new_letter
    if(new_letter == "Y"):
        g = 1
        gravity()
def start_gravity_z():
    global g
    global new_letter
    if(new_letter == "Z"):
        g = 1
        gravity()
length = 25
length -= 1
new_letter = letters.pop(rndm.randint(0, length))
def draw_apple(active_apple):
    active_apple.shape(apple_image)
    wn.update()
    draw_letter()
def draw_letter():
    global new_letter
    letter.goto((apple.xcor() - 23), (apple.ycor() - 47))
    letter.write(new_letter, font=("Arial", 54, "bold"))
g = 0
ground = -180
def gravity():
    global g
    if(g == 1):
        letter.clear()
        while(g == 1):
            if(apple.ycor() >= -180):
                apple.sety(apple.ycor() - 7)
            if(apple.ycor() <= ground):
                g = 0
                move_apple(apple)

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
def move_apple(trtl):
    global new_letter
    global length
    new_apple_x = rndm.randint(-180, 150)
    new_apple_y = rndm.randint(-50, 180)
    apple.goto(new_apple_x, new_apple_y)
    new_letter = letters.pop(rndm.randint(0, length))
    length -= 1
    draw_letter()

draw_apple(apple)

wn.listen()
wn.onkeypress(start_gravity_a, "a")
wn.onkeypress(start_gravity_b, "b")
wn.onkeypress(start_gravity_c, "c")
wn.onkeypress(start_gravity_d, "d")
wn.onkeypress(start_gravity_e, "e")
wn.onkeypress(start_gravity_f, "f")
wn.onkeypress(start_gravity_g, "g")
wn.onkeypress(start_gravity_h, "h")
wn.onkeypress(start_gravity_i, "i")
wn.onkeypress(start_gravity_j, "j")
wn.onkeypress(start_gravity_k, "k")
wn.onkeypress(start_gravity_l, "l")
wn.onkeypress(start_gravity_m, "m")
wn.onkeypress(start_gravity_n, "n")
wn.onkeypress(start_gravity_o, "o")
wn.onkeypress(start_gravity_p, "p")
wn.onkeypress(start_gravity_q, "q")
wn.onkeypress(start_gravity_r, "r")
wn.onkeypress(start_gravity_s, "s")
wn.onkeypress(start_gravity_t, "t")
wn.onkeypress(start_gravity_u, "u")
wn.onkeypress(start_gravity_v, "v")
wn.onkeypress(start_gravity_w, "w")
wn.onkeypress(start_gravity_x, "x")
wn.onkeypress(start_gravity_y, "y")
wn.onkeypress(start_gravity_z, "z")

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
'''for i in range(0, number_of_apples):'''
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.mainloop()
