#Colisiones de la bola
dx = -1
dy = 0

xSpeed = 6
ySpeed = 6

poligono4=canvas2.create_polygon((280,300),(275,270), (150,110),fill="blue")#(x,y)
poligono5=canvas2.create_polygon((450,300),(460,300), (460,350),fill="yellow")#(x,y)

polig = [

        [280, 300], [275, 270], [150, 110], [280, 300],
         
        [450, 300], [460, 300], [460, 350], [450, 300]

         ]



def PointInPolygon(x, y, lista):
    nvert = len(lista)
    c = False
    j = 0
    for i in range(0, nvert - 1):
        j += 1
        ##for j in range(0, nvert - 1):
        if ( ( (lista[i][1] >= y ) != (lista[j][1] >= y) ) and (x <= (lista[j][0] - lista[i][0]) * (y - lista[i][1]) / (lista[j][1] - lista[i][1]) + lista[i][0])):
            c = not c
    return c

def mirarColisiones():
    global dx, dy
    x1, y1, x2, y2 = canvas2.coords(circulo)
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    if (x < 30):
        dx = 1
    if (x > 535):
        dx = -1

    if (y < 60):
        dy = 1
    if (y > 515):
        dy = -1
    

    if PointInPolygon(x1, y1, polig) or PointInPolygon(x2, y2, polig):
        dx *= -1
        dy *= -1
        print("DENTROO")
        
    xSpeed = 3
    ySpeed = 6
    
    if (dy == 1):
        ySpeed = 3
        
    canvas2.move(circulo, dx * xSpeed, dy * ySpeed)
    canvas2.after(1, mirarColisiones)
