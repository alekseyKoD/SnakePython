import time
import turtle


# начальные значения для игры
xScreenSize=1200
yScreenSize=800
snakeHead=15
snakeHeadColor=(255,255,0)
snakePosX=0
snakePosY=0
FPS=10
deltaX=snakeHead
deltaY=snakeHead

#направление движения:
# +1 вправо или вверх
# 0  запрет изменения по координате
# -1 влево или вниз


directionX=1
directionY=1
borderWidth=snakeHead

# Настройка экрана
screen = turtle.Screen()
screen.setup(xScreenSize, yScreenSize)

# 1. ОТКЛЮЧАЕМ АВТО-ОТРИСОВКУ (убирает мерцание)
screen.tracer(0)
snake = turtle.Turtle()
snake.hideturtle()  # Скрываем саму черепашку для ускорения
snake.speed(0)
snake.penup()
turtle.colormode(255)

def moveUp():
    global directionY
    if(directionY==-1):
        directionY=1


def moveDown():
    global directionY
    if (directionY == 1):
        directionY = -1


def moveRight():
    global  directionX
    if(directionX==-1):
        directionX=1


def moveLeft():
    global directionX
    if (directionX == 1):
        directionX = -1



# настраиваем управление
screen.listen()



# Главный игровой цикл
while True:
    snake.clear()  # Очищаем предыдущий кадр


    #---------------отслеживаем нажатия клавиш)

    screen.onkey(moveUp,'W')
    screen.onkey(moveDown, 'S')
    screen.onkey(moveUp, 'w')
    screen.onkey(moveDown, 's')
    screen.onkey(moveRight, 'D')
    screen.onkey(moveLeft, 'A')
    screen.onkey(moveRight, 'd')
    screen.onkey(moveLeft, 'a')




    #---------проверка столкновений с границами экрана------
    if (abs(snakePosX)>=(xScreenSize/2-(snakeHead+borderWidth)) or
            abs(snakePosY)>=(yScreenSize/2-(snakeHead+borderWidth))):
        deltaX=0
        deltaY = 0
    #-------------------------------------------------------

    # -------трансформация змейки------
    snake.goto(snakePosX, snakePosY-snakeHead)
    snakePosX += deltaX*directionX
    snakePosY += deltaY*directionY
    # --------------------------------

    # -------отрисовка змейки----------
    snake.pendown()
    snake.color('black', snakeHeadColor)
    snake.begin_fill()
    snake.circle(snakeHead)
    snake.end_fill()
    snake.penup()
    #----------------------------------

    print(deltaY)





    screen.update() # обновляем
    # Небольшая задержка, чтобы анимация не летела слишком быстро
    time.sleep(1/FPS)




    # turtle.mainloop()