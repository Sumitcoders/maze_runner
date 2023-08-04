from turtle import position
from ursina import *
#@Sumitcoders

level = int(input("Select diffuciulty level:\n1:easy\n2:medium\n3:hard\n4:a bit hard\n5:xtreme hard\n"))
if level == 1:
    __camera_level_alevtion__ = -10
elif level == 2:
    __camera_level_alevtion__ = -7
elif level >= 3:
    __camera_level_alevtion__ = -5





app = Ursina()
app.level = 1

class tst_button(Entity):
    def __init__(self,position,scale = (1,1)):
        
        super().__init__(
            model = 'quad',
            scale = scale,
            color = color.blue,
            position = position

        )
    def input(self,key):
        if key == 'space':
            if p.X == self.X and p.Y == self.Y and self.color == color.blue:
                self.color = color.green
                if app.level == 1:
                    if map[9 - self.Y][self.X  + 24] == 5:
                        map[9 - self.Y][self.X  + 24] = 4
                        
            elif p.X == self.X and p.Y == self.Y and self.color == color.green:
                self.color = color.blue
                if map[9 - self.Y][self.X + 24] == 4:
                    map[9 - self.Y][self.X  + 24] = 5
                    button_pressed()
                    print(map[9 - self.Y][self.X + 24])
            

def button_pressed():
    if app.level == 1:
        if map[9][28] == 5:
            map[4][25] = 0


def update():
    if level < 4:
        c.speed = 0
        c.y = -100
    
    
    
    p.xcor = p.X+24
    p.ycor = 9 - p.Y
    de = time.dt
    #collisions
        


        

    if held_keys['w'] and p.u == True:
        p.y += p.speed * de
    
    if held_keys['a'] and p.l == True:
        p.x -= p.speed * de
    
    if held_keys['d'] and p.r == True:
        p.x += p.speed * de

    if held_keys['s'] and p.d == True:
        p.y -= p.speed * de

    


    u.x = p.x
    u.y = p.y + 0.25
    u.xcor = u.X+24
    u.ycor = 9 - u.Y

    d.x = p.x
    d.y = p.y - 0.25
    d.xcor = d.X+24
    d.ycor = 9 - d.Y

    l.x = p.x - 0.25
    l.y = p.y 
    l.xcor = l.X+24
    l.ycor = 9 - l.Y

    r.x = p.x + 0.25
    r.y = p.y 
    r.xcor = r.X+24
    r.ycor = 9 - r.Y


    


    coll()
    camera.x = p.x
    camera.y = p.y   




    if held_keys['escape']:
        quit()
    
    

def coll():
    if map[u.ycor][u.xcor] == 1:
        p.u = False
    else:
        p.u = True
   
    if map[d.ycor][d.xcor] == 1:
        p.d = False
    else:
        p.d = True
    
    if map[l.ycor][l.xcor] == 1:
        p.l = False
    else:
        p.l = True
    
    if map[l.ycor][l.xcor] == 1:
        p.l = False
    else:
        p.l = True
    if map[r.ycor][r.xcor] == 1:
        p.r = False
    else:
        p.r = True
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if app.level == 1:
        if p.xcor == 48 and p.ycor == 18:
            if held_keys['space']:
                quit()
        if p.xcor == 1 and p.ycor == 1:
            if held_keys['space']:
                p.x = -23
                p.y = -9
    hit = c.intersects()
    if hit.hit:
        c.chasing = False
        c.h -= int(1)

    if c.h < 0:
        p.speed = 0
    else:
        c.chasing = True
    p.xc = c.x-p.x
    p.yc = c.y-p.y
    c.timer -=1
    if c.timer >0:
        c.chasing = False
    if c.chasing == True:
        if p.xc < -0.1:
            c.x = c.x + c.speed*time.dt
        elif p.xc > 0.1:
            c.x = c.x - c.speed*time.dt
        if p.yc < -0.1:
            c.y = c.y + c.speed*time.dt
        elif p.yc > 0.1:
            c.y = c.y - c.speed*time.dt
    
    
    
        
        


map = [
# -23                                            0
#0,1,2,3,4,5,6,7,8,910111213141516171819202122232425262728293031323334353637383940414243444546474849
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #0
[1,3,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1], #1
[1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1], #2
[1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1], #3
[1,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,1], #4
[1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1], #5
[1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1], #6
[1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1], #7
[1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1], #8
[1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1], #9
[1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1], #11
[1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1], #11
[1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1], #12
[1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1], #13
[1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1], #14
[1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1], #15
[1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1], #16
[1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1], #17
[1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,3,1], #18
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  #19
]




p = Entity(model = 'circle', color = color.blue, scale = 0.5, collider = 'sphere', position = Vec3(0,0,0))
p.u = True
p.d = True
p.l = True
p.r = True
p.speed = 6


u = Entity(model = 'quad', color = color.blue,scale = 0.05)
d = Entity(model = 'quad', color = color.blue,scale = 0.05)
l = Entity(model = 'quad', color = color.blue,scale = 0.05)
r = Entity(model = 'quad', color = color.blue,scale = 0.05)
u.visible = False
r.visible = False
l.visible = False
d.visible = False


c = Entity(model = 'circle', color = color.red, scale = 0.5, collider = 'sphere', position = Vec3(-3,0,0))
c.speed = 2

c.chasing = True
if level >4:
    c.h = int(8)
    c.speed = 4



c.h = int(15)


c.timer = int(10)


def load_map():
        
    if app.level == 1:
        ground = Entity(model = 'quad', color = color.gray , scale = (50,20), position = (0.5,-0.5, 1))
        global wall
        for i in range(20):
            for j in range(50):
                if map[i][j] == 1:
                    if 9 - i < 0 and j - 24  > 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,1),position = ((j - 24) + 0.5, (9 - i) - 0.5,0),texture = 'brick')
                    elif 9 - i < 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,1),position = ((j - 24) - 0.5 , (9 - i) - 0.5,0),texture = 'brick')
                    elif 9 - i > 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,1),position = ((j - 24) + 0.5, (9 - i) + 0.5,0),texture = 'brick')
                    elif 9 - i > 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,1),position = ((j - 24) - 0.5, (9 - i) + 0.5,0),texture = 'brick')
                    elif 9 - i == 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,2),position = ((j - 24) + 0.5, (9 - i),0),texture = 'brick')
                    elif 9 - i == 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (1,2),position = ((j - 24) - 0.5, (9 - i),0),texture = 'brick')
                    elif j - 24 == 0 and 9 - i > 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (2,1),position = ((j - 24), (9 - i) + 0.5,0),texture = 'brick')
                    elif j - 24 == 0 and 9 - i < 0:
                        wall = Entity(model = 'quad', color = color.lime, scale = (2,1),position = ((j - 24), (9 - i) - 0.5,0),texture = 'brick')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
                
                elif map[i][j] == 0:
                    if 9 - i < 0 and j - 24  > 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,1),position = ((j - 24) + 0.5, (9 - i) - 0.5,0),texture = 'brick')
                    elif 9 - i < 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,1),position = ((j - 24) - 0.5 , (9 - i) - 0.5,0),texture = 'brick')
                    elif 9 - i > 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,1),position = ((j - 24) + 0.5, (9 - i) + 0.5,0),texture = 'brick')
                    elif 9 - i > 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,1),position = ((j - 24) - 0.5, (9 - i) + 0.5,0),texture = 'brick')
                    elif 9 - i == 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,2),position = ((j - 24) + 0.5, (9 - i),0),texture = 'brick')
                    elif 9 - i == 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (1,2),position = ((j - 24) - 0.5, (9 - i),0),texture = 'brick')
                    elif j - 24 == 0 and 9 - i > 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (2,1),position = ((j - 24), (9 - i) + 0.5,0),texture = 'brick')
                    elif j - 24 == 0 and 9 - i < 0:
                        wall = Entity(model = 'quad', color = color.color(0,0,random.uniform(0.9,1)), scale = (2,1),position = ((j - 24), (9 - i) - 0.5,0),texture = 'brick')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                

                elif map[i][j] == 4:
                    if 9 - i < 0 and j - 24  > 0:
                        button = tst_button(position = ((j - 24) + 0.5, (9 - i) - 0.5,0), scale = (1,1))
                    elif 9 - i < 0 and j - 24 < 0:
                        button = tst_button(position = ((j - 24) - 0.5 , (9 - i) - 0.5,0), scale = (1,1))
                    elif 9 - i > 0 and j - 24 > 0:
                        button = tst_button(position = ((j - 24) + 0.5, (9 - i) + 0.5,0), scale = (1,1))
                    elif 9 - i > 0 and j - 24 < 0:
                        button = tst_button(position = ((j - 24) - 0.5, (9 - i) + 0.5,0), scale = (1,1))
                    elif 9 - i == 0 and j - 24 > 0:
                        button = tst_button(position = ((j - 24) + 0.5, (9 - i),0), scale = (1,2))
                    elif 9 - i == 0 and j - 24 < 0:
                        button = tst_button(position = ((j - 24) - 0.5, (9 - i),0), scale = (1,2))
                    elif j - 24 == 0 and 9 - i > 0:
                        button = tst_button(position = ((j - 24), (9 - i) + 0.5,0), scale = (2,1))
                    elif j - 24 == 0 and 9 - i < 0:
                        button = tst_button(position = ((j - 24), (9 - i) - 0.5,0), scale = (2,1))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                elif map[i][j] == 3:
                    if 9 - i < 0 and j - 24  > 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,1),position = ((j - 24) + 0.5, (9 - i) - 0.5,0))
                    elif 9 - i < 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,1),position = ((j - 24) - 0.5 , (9 - i) - 0.5,0))
                    elif 9 - i > 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,1),position = ((j - 24) + 0.5, (9 - i) + 0.5,0))
                    elif 9 - i > 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,1),position = ((j - 24) - 0.5, (9 - i) + 0.5,0))
                    elif 9 - i == 0 and j - 24 > 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,2),position = ((j - 24) + 0.5, (9 - i),0))
                    elif 9 - i == 0 and j - 24 < 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (1,2),position = ((j - 24) - 0.5, (9 - i),0))
                    elif j - 24 == 0 and 9 - i > 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (2,1),position = ((j - 24), (9 - i) + 0.5,0))
                    elif j - 24 == 0 and 9 - i < 0:
                        wall = Entity(model = 'quad', color = color.yellow, scale = (2,1),position = ((j - 24), (9 - i) - 0.5,0))

load_map()
camera.z = __camera_level_alevtion__

app.run()
