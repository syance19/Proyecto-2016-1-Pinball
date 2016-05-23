from tkinter import *
# creates window
window = Tk()
size = window.winfo_screenheight()
window.title("This is a window")
# set up geometry using string formatting operator %
window.geometry("%dx%d+%d+%d" % (1000, 1000, 10, 10))
window.update()
# creates canvas
global canvas
canvas = Canvas(window, bg='green')
# pack is a layout manager
canvas.pack(fill=BOTH, expand=1)
canvas.update()
canvas.create_rectangle(0, 1000, 1000, 0, fill="orange", width=10, outline="white", tag="border")

def shooting():
    global loaded_gun

    c = canvas.coords("player")
    canvas.create_line(c[0],c[1] + 20,c[2],c[3],width=5,fill="yellow",tag="shot")
    loaded_gun = 0
    move_shot("shot") # furas


def move_shot(name):

    canvas.move(name,0,-10)
    canvas.update()
    window.after(50, move_shot, "shot") # furas

    global loaded_gun

    ran = len(enemies)

    if loaded_gun == 0:
        for x in range(0,ran):

            shot = canvas.coords(name)
            en = canvas.coords(enemies[x])




            if shot[0] == en[0] and shot[0] <= en[0] + 70:
                if shot[1] <= en[1] + 70:
                    #print(canvas.coords(enemies[x]))
                    canvas.delete(enemies[x])
                    #print(canvas.coords(name))
                    enemies.remove(enemies[x])
                    canvas.delete(name)
                    loaded_gun = 1
                    break





def on_key_press(event):

    global canvas,loaded_gun


    c = canvas.coords("player")

    if event.keysym == 'Left' and c[0] > 0:
        canvas.move("player", -20,0)
    elif event.keysym == 'Right' and c[2] < 1000:
        canvas.move("player", 20, 0)
    elif event.keysym == 'space':
        if loaded_gun == 1:
            shooting()
    elif event.keysym == 'Shift_L':
        loaded_gun = 1
        canvas.delete("shot")

def draw_enemy():
    c = [100,100,170,170]
    inc = 100

    global enemies

    enemies = []

    for x in range(0,8):
        for y in range(0,4):
            enemy = canvas.create_rectangle(c[0] + inc * x,c[1] + inc * y,c[2] + inc * x,c[3] + inc * y,fill="red",tag="enemy")
            enemies.append(enemy)

def move_enemy():
    canvas.move("enemy",0,20)
    window.after(1000, move_enemy) # furas


canvas.create_line(500, 950,500,1000, width=15, fill="red",tag="player")

loaded_gun = 1

draw_enemy()

window.bind_all('<Key>', on_key_press) # furas

move_shot("shot") # furas
move_enemy() # furas

window.mainloop()
