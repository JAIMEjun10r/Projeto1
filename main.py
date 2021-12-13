import requests
from tkinter import *
import pyautogui as pg
from time import sleep
import AC
import ALRS
import CAS
import CE
import CO
#criação da interface com o TK

janela = Tk()
janela.title('Programa para abrir matérias da Faculdade')
janela.geometry('400x400')
janela.resizable(width=0, height=0)

text_ori = Label(janela, text='Escolha uma matéria', font='helvetica 17 bold')
text_ori.pack()
text_ori.grid(column=0, row=0)

#criando o botão
ac = Button(janela, text='Arquitetura de Computadores', command=AC.arquitetura_de_computadores)
ac.grid(column=0, row=1, padx=60, pady=10)

alrs = Button(janela, text='Análise e Levantamento de Requisitos de Software', command=ALRS.analise_e_levantamento)
alrs.grid(column=0, row=2, padx=60, pady=10)

co = Button(janela, text='Coaching e Planejamento de Carreira', command=CO.coaching)
co.grid(column=0, row=3, padx=60, pady=10)

cas = Button(janela, text='Criação de Aplicação de Sistemas', command=CAS.criacao_de_sistemas)
cas.grid(column=0, row=4, padx=60, pady=10)

ce = Button(janela, text='Comunicação Empresarial', command=CE.comunicacao_empresarial)
ce.grid(column=0, row=5, padx=60, pady=10)
janela.mainloop()