import turtle
import time
import random

# Pencereyi açma
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Skor
score = 0
target_scores = [500, 1000, 5000]

# Yılan kafası
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Yemek
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Skor yazısı
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Yılanın hareketi
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klavye kontrolleri
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()

    # Yılanın sınırları
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        score_pen.clear()
        score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))
        head.color("white")

    # Yemek yeme kontrolü
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        score_pen.clear()
        score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))

        if score in target_scores:
            if score == 10:
                head.color("yellow")
            elif score == 1000:
                head.color("blue")
            elif score == 5000:
                wn.bye()  # Oyunu kapat

    # Yılanın kuyruğunu takip etme
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Kendine çarpma kontrolü
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            score_pen.clear()
            score_pen.write("Skor: {}".format(score), align="center", font=("Courier", 24, "normal"))
            head.color("white")

    time.sleep(0.1)
