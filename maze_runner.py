from ursina import *
import customtkinter as ctk
#@Sumitcoders

level = int(input("Select diffuciulty level:\n1:easy\n2:medium\n3:hard\n4:a bit hard\n5:xtreme hard\n"))

#Commands



def Title_screen():

    Title_screen = ctk.CTk()
    Title_screen.geometry("500x600+450+50")
    title_frame = ctk.CTkFrame(Title_screen)
    title_frame.pack(padx=30,pady=30)
    Title = ctk.CTkLabel(title_frame,text="Maze Runner\U0001F3C3",font=("Crusive",50))
    Title.pack(padx=50,pady=50)
    btn_frame = ctk.CTkFrame(Title_screen)
    btn_frame.pack(padx=50,pady=50)
    play_btn = ctk.CTkButton(btn_frame,text="PLAY \U000025B6",font=("Cursive",30),command=Title_screen.destroy)
    play_btn.pack(padx=15,pady=10)
    help_btn = ctk.CTkButton(btn_frame,text="Help \U0001F6E0",font=("Cursive",30))
    help_btn.pack(padx=20,pady=20)
    exit_btn = ctk.CTkButton(btn_frame,text="Exit \U0000292B",font=("Cursive",30),command=exit)
    exit_btn.pack(padx=20,pady = 20)


    Title_screen.mainloop()
    level_selctor()
def lvl_set_1():
    global level
    level = 1
    print(level)
def lvl_set_2():
    global level
    level = 2
    print(level)
def lvl_set_3():
    global level
    level = 3
    print(level)
def lvl_set_4():
    global level
    level = 4
    print(level)
def lvl_set_5():
    global level
    level = 5
    print(level)
def level_selctor():
    
    lvl_selector = ctk.CTk()
    text = ctk.CTkLabel(lvl_selector,text="Select Level",font=("Cursive",50))
    text.pack(padx=50,pady=50)
    lvl_1 = ctk.CTkButton(lvl_selector,text="Level 1",command=lvl_set_1)
    lvl_1.pack(padx=50,pady=10)
    lvl_2 = ctk.CTkButton(lvl_selector,text="Level 2",command=lvl_set_2)
    lvl_2.pack(padx=50,pady=10)
    lvl_3 = ctk.CTkButton(lvl_selector,text="Level 3",command=lvl_set_3)
    lvl_3.pack(padx=50,pady=10)
    lvl_4 = ctk.CTkButton(lvl_selector,text="Level 4",command=lvl_set_4)
    lvl_4.pack(padx=50,pady=10)
    lvl_5 = ctk.CTkButton(lvl_selector,text="Level 5",command=lvl_set_5)
    lvl_5.pack(padx=50,pady=10)
    
    
    

    lvl_selector.mainloop()

Title_screen()
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
    if p.hovered == True:
        p.color = color.red
    else:
        p.color = color.blue
    if level < 4:
        c.speed = 0
        c.y = -100
#    print(hitpoint.x,hitpoint.y,hitpoint.z,"_______",camera.x,camera.y,camera.z)
    
    
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
                winscreen()
                
                
        if p.xcor == 1 and p.ycor == 1:
            if held_keys['space']:
                p.x = -23
                p.y = -9
    hit = c.intersects()
    if hit.hit and c.h > 0:
        c.chasing = False
        c.h -= int(1)
        hitpoint.text = str(c.h)

    if c.h == 0:
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
    if p.speed == 0:
        pass
    
    
    
        
        


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
[1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1], #7
[1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,1,0,1], #8
[1,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,1], #9
[1,0,1,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,1], #11
[1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1], #11
[1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1], #12
[1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1], #13
[1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,1], #14
[1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1], #15
[1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1], #16
[1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1], #17
[1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,3,1], #18
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  #19
]

a = Text()
def pause_handeler_input(key):
    
    if key == 'escape':
        if p.speed != 0:
            application.paused = not application.paused
            if application.paused == True:
                a.scale = 4
                a.x = -0.2
                a.text = "PAUSED"
            else:
                a.text = " "
        else:
            quit()
        
    




#pause system
pause_handeler = Entity(ignore_paused = True)
pause_handeler.input = pause_handeler_input


#player
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


if level >3:
    hitpoint = Text(text=str(c.h),x=0.68,scale=4,y=0.4,z=-1)

def load_map():
        
    if app.level == 1:
        ground = Entity(model = 'quad', color = color.gray , scale = (50,20), position = (0.5,-0.5, 1))
        global wall1
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
def winscreen():
    winner_screen = ctk.CTk()

    frame = ctk.CTkFrame(winner_screen)
    frame.pack(padx=30,pady=30)

    if c.h != 0:
        lable = ctk.CTkLabel(frame,text="\U0001F451You Won!\U0001F451",font=("Roboto",30))
    else:
            lable = ctk.CTkLabel(frame,text="Better luck next time.",font=("Roboto",30))
    lable.pack(padx=30,pady=30)
    


    winner_screen.mainloop()
    quit()
camera.z = __camera_level_alevtion__
#EditorCamera()
app.run()


