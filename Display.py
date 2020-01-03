__author__ = 'nruthen16'
__version__ = "9.6.7"

"""Graphing Calculator with basic calculator functions"""

import turtle
import math
from tkinter import *
from tkinter.ttk import *
from tkinter import Tk, Button, Frame, Entry





class App:

    def __init__(self, window):
        self.root = Tk()                        #set up Frame and Window
        self.window = window
        self.f = Frame(self.window, width=263, height=358)
        root.wm_title("Tkinter Calculator")
        root.configure(background='red',relief=SUNKEN, bd=20)

        self.entrytext = StringVar()            #Entry windows for taking in values
        self.entry = Entry(window, textvariable=self.entrytext).grid(row=0,column=1)

        self.entrytext2 = StringVar()
        self.entry2 = Entry(window, textvariable=self.entrytext2).grid(row=1, column=1)


        #Buttons:

        self.button = Button(window, text="Quit", command=window.quit)
        self.button.grid(row=1, column=2)

        self.hi_there = Button(window, text="Hello", command=self.say_hi)
        self.hi_there.grid(row=1, column=0)

        self.instructions = Button(window, text="Instructions", command= lambda: self.intruct())
        self.instructions.grid(row=2, column=1)

        self.add = Button(window, text="    +     ", command= lambda: self.addition())
        self.add.grid(row=3, column=0)

        self.sub = Button(window, text="     -     ", command= lambda: self.subtraction())
        self.sub.grid(row=4, column=0)

        self.multi = Button(window, text="     *     ",  command= lambda: self.multiplication())
        self.multi.grid(row=3, column=2)

        self.divi = Button(window, text="     /     ",  command= lambda: self.division())
        self.divi.grid(row=4, column=2)

        self.expnt = Button(window, text="    ^     ", command= lambda: self.exponent())
        self.expnt.grid(row=5, column=0)

        self.log = Button(window, text="log(x,BASE)",  command= lambda: self.logarithm())
        self.log.grid(row=5, column=2)

        self.squareroot= Button(window, text="    √     ",  command= lambda: self.square_root())
        self.squareroot.grid(row=6, column=0)

        self.abs = Button(window, text="    | |     ",  command= lambda: self.absolute_value())
        self.abs.grid(row=6, column=2)

        self.fact = Button(window, text="    !      ",  command= lambda: self.factorial())
        self.fact.grid(row=7, column=0)

        self.modulo = Button(window, text="  mod   ",  command= lambda: self.mod())
        self.modulo.grid(row=7, column=2)

        self.sin = Button(window, text="  sin()   ",  command= lambda: self.sine())
        self.sin.grid(row=8, column=2)

        self.cos = Button(window, text="  cos() ",  command= lambda: self.cosine())
        self.cos.grid(row=8, column=0)

        self.tan = Button(window, text="  tan()   ",  command= lambda: self.tangent())
        self.tan.grid(row=9, column=2)

        self.trig = Button(window, text="  Trig   ",  command= lambda: self.trig_functions())
        self.trig.grid(row=9, column=0)

        self.integer = Button(window, text="    Int   ",  command= lambda: self.integer_function())
        self.integer.grid(row=10, column=0)

        self.log2 = Button(window, text="  Log   ", command=self.logarithmic)
        self.log2.grid(row=10, column=2)

        self.abs2 = Button(window, text="   Abs  ", command=self.absolute)
        self.abs2.grid(row=11, column=0)

        self.polynomial = Button(window, text="  Poly  ", command=self.polynomial)
        self.polynomial.grid(row=11, column=2)

        self.label = Label(self.root, text="                                                                         ")
        self.label.pack()



    # Calculating answers using the functions below
    # and the entry window values. Then,configuring them in the answer window.

    def addition(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1 + num2
        self.label.configure(text=result)

    def subtraction(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1 - num2
        self.label.configure(text=result)

    def multiplication(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1 * num2
        self.label.configure(text=result)

    def division(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1 / num2
        self.label.configure(text=result)

    def exponent(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1**num2
        self.label.configure(text=result)

    def logarithm(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = math.log(num1, num2)
        self.label.configure(text=result)

    def absolute_value(self):
        num1 = float(self.entrytext.get())
        result = abs(num1)
        self.label.configure(text=result)

    def square_root(self):
        num1 = float(self.entrytext.get())
        result = math.sqrt(num1)
        self.label.configure(text=result)

    def sine(self):
        num1 = float(self.entrytext.get())
        result = math.sin(num1)
        self.label.configure(text=result)

    def cosine(self):
        num1 = float(self.entrytext.get())
        result = math.cos(num1)
        self.label.configure(text=result)

    def tangent(self):
        num1 = float(self.entrytext.get())
        result = math.tan(num1)
        self.label.configure(text=result)

    def factorial(self):
        num1 = float(self.entrytext.get())
        result = math.factorial(num1)
        self.label.configure(text=result)

    def mod(self):
        num1 = float(self.entrytext.get())
        num2 = float(self.entrytext2.get())
        result = num1%num2
        self.label.configure(text=result)


    def say_hi(self):
        result = "Hello, welcome to Tkinter Calculator! This program works like a regular calculator \n""except that " \
                 "it has the added function of being able to graph a couple basic functions \n""for reference. "       \
                 "These buttons are located towards the bottom of the calculator."

        self.label.configure(text=result)

    def intruct(self):
        result = "To add, subtract, multiply, or divide numbers, enter two \n values in the two entry boxes and then " \
                 "press the button \n of the operation you would like to use. For the other buttons, \n enter one "    \
                 "value in the top entry window and click the button you \n want to use."                              \
                 "The bottom buttons (Int, Poly, Trig, Abs, and Log) are graphing functions;"                          \
                 "\n simply click these buttons to start the function.\n The answers will appear in a small "          \
                 "separate window at the top left corner \n of the main window."

        self.label.configure(text=result)

    # Graphical Functions (Turtle Screen Setup):

    def polynomial(self):
        wn = turtle.Screen()
        terms = float(wn.textinput(
        #title:
        "Polynomial Grapher",
        #prompt:
        "Please enter the largest exponent value of your polynomial."
        ))

        t = turtle.Turtle()
        t.setheading(180)
        t.color("red")
        t.speed(0)
        t.up()
        wn.setup(200, 200, 0, 0)
        t.down()

        #Creates graph paper

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        t.goto(0,0)
        t.left(90)

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        coefficients = []
        exponents = []

        t.color("black")
        for i in range(int(terms) + 1):
            coefficient = float(wn.textinput(
                #title:
                "Polynomial Grapher",
                #prompt:
                "Coefficient of term?"))
            coefficients.append(coefficient)
            exponent = terms - i
            exponents.append(exponent)

        for x in range(-100, 100):
            polynomial = 0

            if x == -100:                           # removes the line from the origin to the starting point
                for n in exponents:
                    polynomial += int(coefficients[n]*(x ** n))     #generates each term of the polynomial
                t.up()
                t.goto(x, polynomial)
            else:
                for n in exponents:
                    t.down()
                    polynomial += int(coefficients[n]*(x ** n))
                    t.goto(x, polynomial)

        wn.mainloop()

        wn.exitonclick()

    def logarithmic(self):
        wn = turtle.Screen()
        base = float(wn.textinput(
            #title:
            "Logarithmic Function Grapher",
            #prompt:
            "Please enter the base of the log function. "))
        shift_x = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the shift value for x from the origin of your equation."))
        shift_y = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the shift value for y from the origin of your equation."))
        stretch_y = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter stretch value for y of your equation."))
        stretch_x = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the stretch value for x of your polynomial."))
        t = turtle.Turtle()
        t.setheading(180)
        t.color("red")
        t.speed(0)
        t.up()
        wn.setup(200, 200, 0, 0)
        t.down()

        #Creates graph paper

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        t.goto(0,0)
        t.left(90)

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        for x in range(-100, 100):
            log_function = 0

            if x > 0:     #removes domain error
                t.down()  #standard form for the equation
                log_function += int(stretch_y*(math.log((stretch_x*x + shift_x), base)) + shift_y)
                t.goto(x, log_function)

        wn.mainloop()

        wn.exitonclick()

    def absolute(self):

        wn = turtle.Screen()
        shift_x = int(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the shift value for x from the origin of your equation."))
        shift_y = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the shift value for y from the origin of your equation."))
        stretch_y = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter stretch value for y of your equation."))
        stretch_x = float(wn.textinput(
            #title:
            "Absolute Value Grapher",
            #prompt:
            "Please enter the stretch value for x of your polynomial."))
        t = turtle.Turtle()
        t.setheading(180)
        t.color("red")
        t.speed(0)
        t.up()
        wn.setup(200, 200, 0, 0)
        t.down()

        #Creates graph paper

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        t.goto(0,0)
        t.left(90)

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        for x in range(-100,100):
            if x == -100:
                a = int(stretch_y*(abs(stretch_x*x + shift_x)) + shift_y)  #standard form for the equation
                t.up()
                t.goto(x,a)
            else:
                a = int(stretch_y*(abs(stretch_x*x + shift_x)) + shift_y)
                t.down()
                t.goto(x,a)
        wn.mainloop()

        wn.exitonclick()

    def trig_functions(self):

        wn = turtle.Screen()
        trig_function = int(wn.textinput(
            #title:
            "Trigonometric Functions",
            #prompt:
            "Choose a function by entering the number next to the function: \n"
            "1. sin(), 2. cos(), or 3. tan()"))


        shift_x = float(wn.textinput(
            #title:
            "Trigonometric Functions Grapher",
            #prompt:
            "Please enter the shift value for x from the origin of your equation."))
        shift_y = float(wn.textinput(
            #title:
            "Trigonometric Functions Grapher",
            #prompt:
            "Please enter the shift value for y from the origin of your equation."))
        stretch_y = float(wn.textinput(
            #title:
            "Trigonometric Functions Grapher",
            #prompt:
            "Please enter stretch value for y of your equation."))
        stretch_x = float(wn.textinput(
            #title:
            "Trigonometric Functions Grapher",
            #prompt:
            "Please enter the stretch value for x of your polynomial."))

        t = turtle.Turtle()
        t.setheading(180)
        t.color("red")
        t.speed(0)
        t.up()
        wn.setup(200, 200, 0, 0)
        t.down()

        #Creates graph paper

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        t.goto(0,0)
        t.left(90)

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        if trig_function == 1:
            for x in range(-100,100):
                if x == -100:
                    a = int(stretch_y*(math.sin(x*stretch_x + shift_x)) + shift_y)   #standard form for the equation
                    t.up()
                    t.goto(x,a)
                else:
                    a = int(stretch_y*(math.sin(x*stretch_x + shift_x)) + shift_y)
                    t.down()
                    t.goto(x,a)

        if trig_function == 2:
            for x in range(-100,100):
                if x == -100:
                    a = int(stretch_y*(math.cos(x*stretch_x + shift_x)) + shift_y)  #standard form for the equation
                    t.up()
                    t.goto(x,a)
                else:
                    a = int(stretch_y*(math.cos(x*stretch_x + shift_x)) + shift_y)
                    t.down()
                    t.goto(x,a)

        if trig_function == 3:
            for x in range(-100,100):
                if x == -100:
                    a = int(stretch_y*(math.tan(x*stretch_x + shift_x)) + shift_y)  #standard form for the equation
                    t.up()
                    t.goto(x,a)
                else:
                    a = int(stretch_y*(math.tan(x*stretch_x + shift_x)) + shift_y)
                    t.down()
                    t.goto(x,a)

    def integer_function(self):
        wn = turtle.Screen()

        shift_x = float(wn.textinput(
            #title:
            "Integer Function Grapher",
            #prompt:
            "Please enter the shift value for x from the origin of your equation."))
        shift_y = float(wn.textinput(
            #title:
            "Integer Function Grapher",
            #prompt:
            "Please enter the shift value for y from the origin of your equation."))
        stretch_y = float(wn.textinput(
            #title:
            "Integer Function Grapher",
            #prompt:
            "Please enter stretch value for y of your equation."))
        stretch_x = float(wn.textinput(
            #title:
            "Integer Function Grapher",
            #prompt:
            "Please enter the stretch value for x of your polynomial."))

        t = turtle.Turtle()
        t.setheading(180)
        t.color("red")
        t.speed(0)
        t.up()
        wn.setup(200, 200, 0, 0)
        t.down()

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        t.goto(0,0)
        t.left(90)

        for i in range(10):
            t.forward(10)
            t.left(90)
            t.forward(3)
            t.backward(3)
            t.right(90)

        t.goto(0,0)

        for i in range(10):
            t.backward(10)
            t.right(90)
            t.backward(3)
            t.forward(3)
            t.left(90)

        for x in range(-100,100):
                if x == -100:
                    a = int(stretch_y*(math.ceil(x*stretch_x + shift_x)) + shift_y)  #standard form for the equation
                    t.up()
                    t.goto(x,a)
                else:
                    a = int(stretch_y*(math.ceil(x*stretch_x + shift_x)) + shift_y)
                    t.down()
                    t.goto(x,a)

        wn.mainloop()

        wn.exitonclick()

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
