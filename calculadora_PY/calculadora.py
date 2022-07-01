from tkinter import *
import tkinter as tk

root = Tk()
root.title('Calculadora')
root.geometry("170x100")
soma = IntVar(root)
parcela = IntVar(root)
parcela2 = IntVar(root)

def somafunc():
    soma.set(soma.get() + parcela.get() + parcela2.get())


def subfunc():
    soma.set(soma.get() + parcela.get() - parcela2.get())


def mutfunc():
    soma.set(soma.get() + parcela.get() * parcela2.get())


def divfunc():
    soma.set(soma.get() + parcela.get() / parcela2.get())


def limpafunc():
    parcela.set(0), parcela2.set(0), soma.set(0)


def arqFunc():
    nomefile = 'teste.txt'
    file = open(nomefile, 'a')
    linha = str(parcela.get()) + ';' + str(parcela2.get()) + '\n'
    file.write(linha)
    file.close()


def leArqFunc():
    nomefile = 'teste.txt'
    file = open(nomefile, 'r')
    for linha in file:
        campos = linha.split(';')
        for elemento in campos:
            parcela.set(campos[0])
            parcela2.set(campos[1])
    file.close()

mais = Button(text='+', font='Arial 10 bold' , command=somafunc)
menos = Button(text='-', font='Arial 10 bold', command=subfunc)
vezes = Button(text='*', font='Arial 10 bold', command=mutfunc)
dividido = Button(text='/', font='Arial 10 bold', command=divfunc)
m = Button(text='M', font='Arial 10', command=arqFunc)
limpar = Button(text='Limpar', font='Arial 10', command=limpafunc)
c = Button(text='C', font='Arial 10', command=leArqFunc)

txtigual = tk.Label(text='=')
text1 = tk.Label(text='Valor1')
lsoma = tk.Label(textvar= soma)
text2 = tk.Label(text='Valor2')
eparcela = tk.Entry(textvar=parcela)
eparcela2 = tk.Entry(textvar=parcela2)


text1.grid(row=1, column=2, columnspan=2)
eparcela.grid(row=1, column=4, columnspan=8)
text2.grid(row=2, column=2, columnspan=2)
eparcela2.grid(row=2, column=4, columnspan=8)
txtigual.grid(row=5, column=5)
lsoma.grid(row=5, column=6)
mais.grid(row=6, column=2)
menos.grid(row=6, column=3)
vezes.grid(row=6, column=4)
dividido.grid(row=6, column=5)
m.grid(row=6, column=6)
limpar.grid(row=6, column=7)
c.grid(row=6, column=8)

mainloop()
