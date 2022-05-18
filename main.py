import turtle
import pandas

screen = turtle.Screen()
screen.title("Estados Brasileiros - Game")
screen.setup(785,710) 
imagem = "estados_brasileiro.gif" # Para adicionar a imagem na tela
screen.addshape(imagem)
turtle.shape(imagem)


#Código para obter as coordenadas (x,y) dos estados no mapa
'''
def get_mouse_click_coor(x, y):
  print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() # para a tela não fechar
'''
dados = pandas.read_csv("states_27.csv")
all_estados = dados.estados.to_list()

lista_usuario = [] #Lista com os estados inseridos pelo usuário

while len(lista_usuario) < 27:
  pergunta = screen.textinput(title=f"{len(lista_usuario)}/27 Estados Corretos", prompt="Digite o nome do Estado").upper()
  pergunta.setposition(-600,-600)

  # Quando sair, criar uma nova lista de estados que faltam
  if pergunta == "Exit":
    estados_não_inseridos = []
    for estados in all_estados:
      if estados not in lista_usuario:
        estados_não_inseridos.append(estados)
    novos_dados = pandas.DataFrame(estados_não_inseridos)
    novos_dados.to_csv("estados_aprender.csv")
    break

  #Para verificar se a resposta inserida é um estado de acordo com a lista
  if pergunta in all_estados:
    lista_usuario.append(pergunta)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("blue")
    novo_estado = dados[dados.estados == pergunta]
    t.goto(int(novo_estado.x), int(novo_estado.y))
    t.write(pergunta)


