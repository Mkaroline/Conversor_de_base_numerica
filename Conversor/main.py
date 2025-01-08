import tkinter
from tkinter import *
from tkinter import ttk

# cores
# cores = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black"]
Co0 = "#444466"  # preta
co1 = "#feffff"  # branco
co2 = "#0033FF"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#008000"  # verde

janela = Tk()
janela.title('')
janela.geometry('400x310')
janela.configure(bg=co1)

# estilo
style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

# Dividindo a janela em dois frames

frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
frame_baixo.grid(row=2, column=0, sticky=NW)

# configurando frame cima
app_nome = Label(frame_cima, text="Conversor de base numérica",
                 relief=FLAT, anchor='center', font=('System 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)


# funcao converter
def Converter():
    # Funcao para converter qualquer numero em
    # uma base para o seu correspondente em DECIMAL
    def numero_para_decimal(numero, base):
        # o numero decimal correspondente
        decimal = int(numero, base)

        binario = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        l_binario['text'] = str(binario[2:])
        l_octal['text'] = str(octal[2:])
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:].upper())

    numero = e_valor.get()
    base = combo.get()

    # definindo o valor da base
    if base == 'BINARIO':
        base = 2
    elif base == 'OCTAL':
        base = 8
    elif base == 'DECIMAL':
        base = 10
    else:
        base = 16

    # chamando a funcao
    numero_para_decimal(numero, base)


# configurando frame baixo
bases = ['BINARIO', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']
combo = ttk.Combobox(frame_baixo, width=12,justify=CENTER, font=('Ivy 12 bold'))
combo['values'] = (bases)
combo.place(x=35, y=10)


e_valor = Entry(frame_baixo, width=9, justify='center', font=(
    "", 13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)


b_convertor = Button(frame_baixo, command=Converter, text="CONVERTER",
                     relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_convertor.place(x=247, y=10)


l_binario = Label(frame_baixo, text="BINARIO", width=12,
                  relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_binario.place(x=35, y=60)
l_binario = Label(frame_baixo, text="", width=13, relief=FLAT,
                  anchor='center', font=('Verdana 13'), fg=co4)
l_binario.place(x=170, y=60)


l_octal = Label(frame_baixo, text="OCTAL", width=12, relief=FLAT,
                anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_octal.place(x=35, y=100)
l_octal = Label(frame_baixo, text="", width=13, relief=FLAT,
                anchor='center', font=('Verdana 13'), fg=co4)
l_octal.place(x=170, y=100)


l_decimal = Label(frame_baixo, text="DECIMAL", width=12,
                  relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_decimal.place(x=35, y=140)
l_decimal = Label(frame_baixo, text="", width=13, relief=FLAT,
                  anchor='center', font=('Verdana 13'), fg=co4)
l_decimal.place(x=170, y=140)


l_hexadecimal = Label(frame_baixo, text="HEXADECIMAL", width=12,
                      relief=FLAT, anchor='nw', font=('Verdana 13'), bg=co5, fg=co1)
l_hexadecimal.place(x=35, y=180)
l_hexadecimal = Label(frame_baixo, text="", width=13,
                      relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_hexadecimal.place(x=170, y=180)


janela.mainloop()
