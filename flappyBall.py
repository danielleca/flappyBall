import pgzrun, random
TITLE="FlappyBall"
WIDTH=600
HEIGHT=600
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
clr=r,g,b
GRAVITY=2000.0 #pixels per second

class Ball:
    def __init__(self,x,y):
        self.initialx=x
        self.initialy=y
        self.vx=200
        self.vy=0
        self.radius=40
    def draw(self):
        pos=(self.initialx,self.initialy)
        screen.draw.filled_circle(pos, self.radius, clr)
b1=Ball(80,80)
def draw():
    screen.clear()
    b1.draw()
def update(dt):
    uy=b1.vy
    b1.vy+=GRAVITY*dt
    b1.initialy+=(uy+b1.vy)*0.5*dt   
    if b1.initialy>HEIGHT-b1.radius:
        b1.initialy=HEIGHT-b1.radius
        b1.vy=-b1.vy*0.9 #Inelastic collision
    b1.initialx+=b1.vx*dt
    if b1.initialx>WIDTH-b1.radius or b1.initialx<b1.radius:
        b1.vx=-b1.vx
def on_key_down(key):
    if key==keys.SPACE:
        b1.vy=-500
pgzrun.go()
