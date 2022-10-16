import turtle as t
t.fillcolor("red")
t.begin_fill()
while(1):
    t.forward(200)
    t.right(144)
    if abs(t.pos()) < 1:
        break
t.end_fill()