import turtle as t

def HSB2RGB(hues):
    hues = hues * 3.59 #100转成359范围
    rgb=[0.0, 0.0, 0.0]
    i = int(hues / 60) % 6
    f = hues / 60 - i
    if i == 0: 
        rgb[0] = 1;
        rgb[1] = f;
        rgb[2] = 0;
    elif i == 1:
        rgb[0] = 1 - f;
        rgb[1] = 1;
        rgb[2] = 0;
    elif i == 2:
        rgb[0] = 0;
        rgb[1] = 1;
        rgb[2] = f;
    elif i == 3:
        rgb[0] = 0;
        rgb[1] = 1 - f;
        rgb[2] = 1;
    elif i == 4:
        rgb[0] = f;
        rgb[1] = 0;
        rgb[2] = 1;
    elif i == 5:
        rgb[0] = 1;
        rgb[1] = 0;
        rgb[2] = 1 - f;
    return rgb

def rainbow():
    hues = 0.0
    t.color(1, 0, 0)
    #绘制彩虹
    t.hideturtle()
    t.speed(100)
    t.pensize(3)
    t.penup()
    t.goto(-400, -300)
    t.pendown()
    t.right(110)
    for i in range (100):
        t.circle(1000)
        t.right(0.13)
        hues = hues + 1
        rgb = HSB2RGB(hues)
        t.color(rgb[0], rgb[1], rgb[2])
    t.penup()

def main():
    t.setup(800, 600, 0, 0)
    t.bgcolor(0.8, 0.8, 1.0)
    t.tracer(False)
    rainbow()
    #输出文字
    t.goto(100, -100)
    t.pendown()
    t.color("red")
    t.write("Rainbow", align="center", font=("Script MT Bold", 80, "bold"))
    t.tracer(True)
    t.mainloop()