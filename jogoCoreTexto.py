# modulos para GUI
import tkinter
# modulos para nums aleatorios
import random

# lista de cores possiveis
cores = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']

placar=0
tempoRestante=30

# funcao que comeca o jogo
def startGame(event):

    if tempoRestante == 30:
        # começa o contador
        countdown()

    # chama a função que pede a proxima cor
    proximaCor()

# função para escolher e mostrar a prox cor
def proximaCor():

    # usa as variaveis globais placar e tempoRestante
    global placar
    global tempoRestante

    # se o jogo ainda estiver rodando
    if tempoRestante > 0:

        # faz com que o campo de texto fique ativo
        e.focus_set()

        # se a cor escrita for igual a cor do texto
        if e.get().lower() == cores[1].lower():
            # add um ao placar
            placar += 1

        # limpa a entrada do texto
        e.delete(0, tkinter.END)
        # mistura a lista de cores
        random.shuffle(cores)
        # muda a cor para digitar, mudando o texto e a cor para um valor aleatorio
        label.config(fg=str(cores[1]), text=str(cores[0]))
        # atualiza o placar
        placarLabel.config(text="Placar: " + str(placar))

# contador
def countdown():

    # variavel global tempoRestante
    global tempoRestante

    # se o jogo estiver rodando
    if tempoRestante > 0:

        # decrementa um do timer
        tempoRestante -= 1
        # atualiza o texto do timer
        tempoLabel.config(text="Tempo restante: " + str(tempoRestante))
        # roda a função novamente apos um segundo
        tempoLabel.after(1000, countdown)

# cria janela GUI
root = tkinter.Tk()
# titulo
root.title("Cor e Texto")
# tamanho da tela
root.geometry("375x200")

# instruções
instrucoes = tkinter.Label(root, text="Digite a cor das palavras, e não a palavra!", font=('Helvetica', 12))
instrucoes.pack()

# label placar
placarLabel = tkinter.Label(root, text="Pressione enter para iniciar", font=('Helvetica', 12))
placarLabel.pack()

# label tempo
tempoLabel = tkinter.Label(root, text="Tempo restante: " + str(tempoRestante), font=('Helvetica', 12))
tempoLabel.pack()

# label para mostrar as cores
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# entrada de texto para digitar as cores
e = tkinter.Entry(root)
# inicia o jogo quando ENTER é pressionado
root.bind('<Return>', startGame)
e.pack()
# libera digitação na caixa de texto
e.focus_set()

# inicia o GUI
root.mainloop()
