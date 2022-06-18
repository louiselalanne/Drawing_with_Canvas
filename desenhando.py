from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Desenhando no canvas')
root.geometry('600x600')
root.config(background="lightcoral")

cor_label = Label(root, text="Digite a cor: ", bg="lightcoral")
cor_label.place(relx=0.6, rely=0.9, anchor=CENTER)

text_input = Entry(root)
text_input.insert(0,"black")
text_input.place(relx=0.8, rely=0.9, anchor=CENTER)

canvas = Canvas(root, width=590, height=510, bg="snow2", highlightbackground="palegreen")

lapis = ImageTk.PhotoImage(Image.open("lapis.png"))
imagem = canvas.create_image(50, 50, image=lapis)

direcao = ""
oldx = 50
oldy=70
newx=50
newy=70

def right_dir(event):
    global direcao
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx + 5
    direcao = "right"
    draw(direcao, oldx, oldy, newx, newy)

def left_dir(event):
    global direcao
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx - 5
    direcao = "left"
    draw(direcao, oldx, oldy, newx, newy)

def up_dir(event):
    global direcao
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy - 5
    direcao = "up"
    draw(direcao, oldx, oldy, newx, newy)

def down_dir(event):
    global direcao
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy + 5
    direcao = "down"
    draw(direcao, oldx, oldy, newx, newy)

def draw (direcao, oldx, oldy, newx, newy):
    fill_color = text_input.get()
    if(direcao=="right"):
        right_line = canvas.create_line(oldx, oldy, newx, newy, width =3, fill = fill_color)
    if (direcao=="left"):
        left_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
    if(direcao=="up"):
        up_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)
    if(direcao=="down"):
        down_line= canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= fill_color)

canvas.pack()    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()