from drawingpanel import *
import time as tiiime
def main():
    panel = DrawingPanel(600, 600)

    ball1x = 100
    ball1y = 0
    v01 = 25
    ball2x = 200
    ball2y = 100
    v02 = 15
    ball3x = 300
    ball3y = 0
    v03 = 30
    ball4x = 400
    ball4y = 100
    v04 = 35
    ball5x = 500
    ball5y = 0
    v05 = 40

    for time in range(0, 90, 1):
        disp1 = displacement(v01, time/10, 9.81)
        panel.canvas.create_oval(ball1x, ball1y + disp1, ball1x + 10, ball1y + 10 + disp1)
        disp2 = displacement(v02, time/10, 9.81)
        panel.canvas.create_oval(ball2x, ball2y + disp2, ball2x + 10, ball2y + 10 + disp2)
        disp3 = displacement(v03, time/10, 9.81)
        panel.canvas.create_oval(ball3x, ball3y + disp3, ball3x + 10, ball3y + 10 + disp3)
        disp4 = displacement(v04, time/10, 9.81)
        panel.canvas.create_oval(ball4x, ball4y + disp4, ball4x + 10, ball4y + 10 + disp4)
        disp5 = displacement(v05, time/10, 9.81)
        panel.canvas.create_oval(ball5x, ball5y + disp5, ball5x + 10, ball5y + 10 + disp5)
        panel.sleep(20)
        # pause for 50 ms
        panel.canvas.create_rectangle(0, 0, 600, 600, fill="white", width=0)

def displacement(velocity,time,acceleration):
    first = velocity*time
    second = acceleration*(time**2)/2
    return first+second

main()
