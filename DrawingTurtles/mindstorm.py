import turtle
import math
import matplotlib
import numpy as np
import PIL.Image
import pygame
from pygame import mixer as mixer
from tkinter import *
import time

mixer.init()
mixer.music.load("/Users/CAO/Pythonia/Udacity_PythonFundamental/DrawingTurtles/material/SummerFirework.mp3")
mixer.music.set_volume(0.4)
mixer.music.play()
# song = mixer.Sound("/Users/CAO/Desktop/SummerFirework.mp3")
# song.play()

# image1 = PIL.Image.open("/Users/CAO/Desktop/bg.png")
# # image2 = PIL.Image.open("/Users/CAO/Desktop/white.png")
# image1 = image1.resize((1100, 700), PIL.Image.ANTIALIAS)
# # PIL.Image.blend(image1, image2, 0.3)
# image1.save("/Users/CAO/Desktop/bg1.png")
# #image1.show()


# im = Image.new("RGBA", (200,200), (255,255,255))
# print(im.getpixel((0,0)))
# im2 = Image.new("RGBA", (200,200), (255,255,255,0))
# print(im2.getpixel((0,0)))


def draw_square(some_turtle):
    for _ in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range (1, 4):
        some_turtle.forward(200)
        some_turtle.right(120)

def draw_diamond(some_turtle):
    for i in range(1, 3):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_fractal_tri(some_turtle, length, depth):
    if depth == 0:
        for _ in range(1, 4):
            some_turtle.fd(length)
            some_turtle.lt(120)
    else:
        draw_fractal_tri(some_turtle, length/2, depth - 1)
        some_turtle.fd(length/2)
        draw_fractal_tri(some_turtle, length/2, depth - 1)
        some_turtle.bk(length/2)
        some_turtle.left(60)
        some_turtle.fd(length/2)
        some_turtle.right(60)
        draw_fractal_tri(some_turtle, length/2, depth - 1)
        some_turtle.left(60)
        some_turtle.bk(length/2)
        some_turtle.right(60)

def draw_dango(some_turtle):
    some_turtle.penup()
    some_turtle.goto(-280,20)
    some_turtle.pensize(30)
    some_turtle.pendown()
    some_turtle.setheading(45)
    some_turtle.fd(80)
    some_turtle.pensize(3)

    some_turtle.right(90)
    some_turtle.color("tomato", "palegreen")
    some_turtle.begin_fill()
    some_turtle.circle(50)
    some_turtle.end_fill()

    some_turtle.penup()
    some_turtle.goto(-280 + 180 // (2**0.5) - 8, 20 + 180 // (2**0.5) - 8)
    some_turtle.pendown()
    some_turtle.color("tomato", "floralwhite")
    some_turtle.begin_fill()
    some_turtle.circle(50)
    some_turtle.end_fill()

    some_turtle.penup()
    some_turtle.goto(-280 + 280 // (2 ** 0.5) - 16, 20 + 280 // (2 ** 0.5) - 16)
    some_turtle.pendown()
    some_turtle.color("tomato", "pink")
    some_turtle.begin_fill()
    some_turtle.circle(50)
    some_turtle.end_fill()

    some_turtle.hideturtle()


def draw_heart(some_turtle):
    # some_turtle.t = np.arange(0, 2 * np.pi, 0.1)
    # some_turtle.x = 16 * np.sin(some_turtle.t) ** 3.
    # some_turtle.y = 13 * np.cos(some_turtle.t) - 5 * np.cos(2 * some_turtle.t) - 2 * np.cos(3 * some_turtle.t) - np.cos(4 * some_turtle.t)
    # some_turtle.matplotlib.pyplot.plot(some_turtle.x, some_turtle.y)
    def curvemove(t):
        for _ in range(200):
            t.right(1)
            t.forward(1)
            # t.speed(0)
    # some_turtle.speed(0)
    some_turtle.penup()
    some_turtle.goto(0, -60)
    some_turtle.pendown()
    some_turtle.begin_fill()
    some_turtle.left(140)
    some_turtle.forward(111.65)
    curvemove(some_turtle)
    some_turtle.left(120)
    curvemove(some_turtle)
    some_turtle.forward(111.65)
    some_turtle.end_fill()
    some_turtle.hideturtle()

def draw_jim(some_turtle):
    some_turtle.penup()
    some_turtle.goto(0, -120)
    some_turtle.pendown()
    some_turtle.pensize(10)
    some_turtle.fd(100)
    some_turtle.bk(50)
    some_turtle.right(90)
    some_turtle.fd(150)
    some_turtle.left(270)
    some_turtle.circle(-100, 45)

    some_turtle.penup()
    some_turtle.goto(0, -120)
    some_turtle.setheading(0)
    some_turtle.fd(140)
    some_turtle.pendown()
    some_turtle.right(90)
    some_turtle.fd(150)

    some_turtle.penup()
    some_turtle.goto(180, -270)
    some_turtle.pendown()
    some_turtle.setheading(90)
    some_turtle.fd(150)
    some_turtle.right(160)
    some_turtle.fd(150 // math.cos(math.pi/9))
    some_turtle.left(140)
    some_turtle.fd(150 // math.cos(math.pi / 9))
    some_turtle.setheading(-90)
    some_turtle.fd(150)


def draw_art():
    window = turtle.Screen()
    window.screensize(1300, 700)
    window.bgpic("/Users/CAO/Pythonia/Udacity_PythonFundamental/DrawingTurtles/material/blend233.gif")
    window.bgcolor("papayawhip")

    # Create the turtle Dango - draw Dango
    dango = turtle.Turtle()
    dango.shape("arrow")
    dango.color("lightcoral")
    dango.speed(4)
    draw_dango(dango)

    # Create the turtle Heart - draw Heart
    heart = turtle.Turtle()
    heart.shape("circle")
    heart.color('red', 'deep pink')
    heart.speed(3)
    draw_heart(heart)

    # Create the turtle Tako - draw Jim
    tako = turtle.Turtle()
    tako.shape("classic")
    tako.color("blue")
    tako.speed(4)
    draw_jim(tako)




    # # Create the turtle Brad - draw a square
    # brad = turtle.Turtle()
    # brad.shape("turtle")
    # brad.color("red")
    # brad.speed(8)
    # for _ in range (1, 37):
    #     draw_square(brad)
    #     brad.right(10)
    #
    # # Create the turtle A - draw a triangle
    # a = turtle.Turtle()
    # a.shape("turtle")
    # a.color("black")
    # draw_triangle(a)
    #
    # # Create the turtle Angie - draw a circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("blue")
    # angie.circle(100)
    #
    # # Create the turtle B - draw a dimond
    # b = turtle.Turtle()
    # b.shape("turtle")
    # b.color("blue")
    # b.speed(0)
    # for _ in range (1, 360 // 8 + 1):
    #     draw_diamond(b)
    #     b.right(8)
    #
    # # Create the turtle C - draw many triangles
    # c = turtle.Turtle()
    # c.shape("turtle")
    # c.color("green")
    # c.speed(0)
    # for _ in range (1, 5):
    #     draw_fractal_tri(c, 400, 4)
    #     c.rt(90)

    window.exitonclick()

# from threading import Thread
# def go():
#     time.sleep(5)
#     mixer.fadeout(5)
#
# Thread(target=go).start()

draw_art()
mixer.fadeout(5)
