guess = input('Who will win? Blue, Purple, or Green: ')

from turtle import *
from time import *
import random
screen = Screen()

OPTIONS = [0.005, 0.007, 0]
DIALOGUE2 = random.choice(['   Awe man I put my life savings on purple', '   My wife\'s gonna kill me\n'
                                                           '   I just bet my entire paycheck',
             '   Show me the moneyyyy!', '     Is this all the world has to offer?'])
DIALOGUE1 = random.choice(['   WAKE UP PURPLE!', '   Why do I always\n   bet on purple...', '   Is he sleeping?'])
DIALOGUE3 = random.choice(['   Let\'s go Green', '   OK Blue I see you!', '   Purple you can still do it!'])
DIALOGUE4 = random.choice(['   Blue you suck!!', '   Green you suck!!', '   I hate my life...'])

screen.bgcolor('#cf4a28')
draw = Turtle()
draw.pencolor('white')

turtle1 = Turtle()
turtle1.shape('turtle')
turtle1.color('green')
turtle2 = Turtle()
turtle2.shape('turtle')
turtle2.color('blue')
turtle3 = Turtle()
turtle3.shape('turtle')
turtle_fan1 = Turtle()
turtle_fan1.shape('turtle')
turtle_fan1.penup()
turtle_fan2 = Turtle()
turtle_fan2.shape('turtle')
turtle_fan2.penup()
turtle_fan3 = Turtle()
turtle_fan3.shape('turtle')
turtle_fan3.penup()
turtle_fan4 = Turtle()
turtle_fan4.shape('turtle')
turtle_fan4.penup()


def draw_track():
    ratio = 1
    draw.speed(0)
    draw.pensize(3)
    for i in range(4):
        draw.penup()
        draw.sety(-300*ratio)
        draw.pendown()
        draw.circle(300*ratio)
        ratio -= .2
    draw.sety(-300)
draw_track()
def get_set():
    #Fans set
    turtle_fan1.setx(250)
    turtle_fan1.sety(250)
    turtle_fan1.right(180)
    turtle_fan2.setx(-250)
    turtle_fan2.sety(250)
    turtle_fan3.setx(-250)
    turtle_fan3.sety(-250)
    turtle_fan4.setx(250)
    turtle_fan4.sety(-250)
    turtle_fan4.right(180)
    #Turtle 1 set
    turtle1.penup()
    turtle1.speed(10)
    ratio = .9
    turtle1.sety(-300*ratio)
    turtle1_radius = 300 * ratio
    # Turtle 2 set
    turtle2.penup()
    turtle2.speed(0)
    ratio = .7
    turtle2.sety(-300 * ratio)
    turtle2.circle(300 * ratio, 257.04)
    turtle2_radius = 300 * ratio
    # Turtle 3 set
    turtle3.penup()
    turtle3.speed(10)
    ratio = .5
    turtle3.sety(-300 * ratio)
    turtle3_radius = 300 * ratio
get_set()
sleep(2)
def go():
    write('Start!',False, align="center", font=('Arial', 10, 'normal'))
    turtle3.color('purple')
    turtle3.write('zzzzzzz')
    turtle1.speed(7)
    turtle2.speed(7)
    t1_extent = 0
    t2_extent = 0
    T1_MAX = 360
    T2_MAX = 462.96

    while t1_extent < T1_MAX and t2_extent < T2_MAX:
        move1_rate = T1_MAX * random.choice(OPTIONS)
        move2_rate = T2_MAX * random.choice(OPTIONS)
        t1_extent += move1_rate
        t2_extent += move2_rate
        move1 = turtle1.circle(270, move1_rate)
        move2 = turtle2.circle(210, move2_rate)
        moves = [move1, move2]
        random.choice(moves)
        if t1_extent > 50 and t1_extent < 100:
            turtle_fan4.write(DIALOGUE4)
        if t1_extent > 100 and t1_extent < 150:
            turtle_fan1.write(DIALOGUE1)
        if t1_extent > 175 and t1_extent < 235:
            turtle_fan2.write(DIALOGUE2)
        if t1_extent >  250 and t1_extent < 360:
            turtle_fan3.write(DIALOGUE3)
    if t2_extent >= T2_MAX and t1_extent >= T1_MAX:
        write('It\'s a tie!', False, align="center", font=('Arial', 30, 'normal'))
        winner = ''
    elif t2_extent >= T2_MAX:
        color('blue')
        clear()
        write('Blue wins!',False, align="center", font=('Arial', 30, 'normal'))
        winner = 'Blue'
    elif t1_extent >= T1_MAX:
        color('green')
        clear()
        write('Green wins!',False, align="center", font=('Arial', 30, 'normal'))
        winner = 'Green'
    if winner == guess:
        penup()
        sety(-10)
        pendown()
        write('You win!',False, align="center", font=('Arial', 10, 'normal'))
    else:
        penup()
        sety(-10)
        pendown()
        write('You lose!',False, align="center", font=('Arial', 10, 'normal'))






go()


sleep(10)
