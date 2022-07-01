from tkinter import *

c = Canvas()
c.pack()
cor = StringVar(c)
cor.set('black')
l = Label(background=cor.get())


def pinta():
    l.configure(background=cor.get())


for txt, val in (('preto', 'black'), ('vermelho', 'red'), ('azul', 'blue'), ('verde', 'green')):
    Radiobutton(text=txt, value=val, variable=cor, command=pinta, indicatoron=False).pack(anchor=W)


def crialinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    c.create_line(x, y, x, y, tags='corrente', fill=cor.get(), width=2)


def estendelinha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    coords = c.coords('corrente') + [x, y]
    c.coords('corrente', *coords)


def fechalinha(e):
    c.itemconfig('corrente', tags=())


def borracha(e):
    x, y = c.canvasx(e.x), c.canvasy(e.y)
    c.create_line(x, y, x, y, tags='corrente', width=10, fill='#f0f0f0')


def fechaborracha(e):
    c.itemconfig('corrente', tags=())


def aumentaborracha(e):
    if e.char == 'a':
        x, y = c.canvasx(e.x), c.canvasy(e.y)
        c.create_line(x, y, x, y, tags='corrente', width=15, fill='#f0f0f0')


def pintaFundo(e):
    c.configure(background=cor.get())
    c.pack(fill='both')


def limpaPagina(e):
    c.configure(background=cor.get())
    c.pack(fill='both')


def criaQuadrado(e):
    quadrado = c.create_rectangle(40, 150, 30, 50, 60, 200, 120, fill=cor.get(), whidth=2)


def colocaImagem(e):
    img = PhotoImage(file='gif.gif')
    imagem = c.create_image(150, 100, image=img, anchor=NW)


def caixaDeTexto(e):
    t = c.create_text(200, 35, text='Texto \ntexto', font='Arial 22')


c.bind('<Button-1>', crialinha)
c.bind('<B1-Motion>', estendelinha)
c.bind('<ButtonRelease-1>', fechalinha)
c.bind('<Button-3>', borracha)
c.bind('<B3-Motion>', estendelinha)
c.bind('<ButtonRelease-3>', fechaborracha)
c.bind('<Shift-Tab>', pintaFundo)
c.bind('<Key>', limpaPagina)

c.pack(fill='both', expand=True)
mainloop()