from random import randint
import replit
#Aluno: João Paulo Cardoso Rodrigues. Curso: DSM, Noite 1° Ano
def menu():
  print("-=-"*12)
  print("1 - Percorrer Palavra ")
  print("2 - Jogo da Quina ")
  print("9 - Finalizar ")
  print("-=-"*12)


def percorrerString():
  """
  Retorna o fatiamento de um frase, com as suas posições no alfabeto
  """
  #Gera os números sem repetir
  numerosAlfa = list()
  cont = 0
  while True:
    numero = randint(1, 26)
    if numero not in numerosAlfa:
      numerosAlfa.append(numero)
      numerosAlfa.sort()
      cont += 1
    if cont >= 26:
      break
  alfa = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  palavra = str(input('\nDigite uma única palvra: ')).strip().upper()# O metodo upper, joga das as letras para maiusculas

  for cont, val in enumerate(alfa):
    print(f'Letra:{val} - Posição{cont+1}')
  

  for indice, valor in enumerate(palavra):
    for posicao, conteudo in enumerate(alfa):
      if valor == conteudo:
        print(f'\nLetra da Palavra: {palavra[indice]} -=- Posição: {indice+1}')
        print(f'Letra do Alfabeto na Posição: {posicao+1}')
        print('~~~~~~~~~~~'*3)

  enter = input('\nPressione ENTER para prosseguir....')





def jogoQuina():
  """
  A lógica do jogo é sortear 5 números que não se repetem
  e adicionar em uma lista
  """
  listaAposta = list()
  cont = 0
  while True:
    numero = randint(1, 60)
    if numero not in listaAposta:
      listaAposta.append(numero)
      cont += 1
    if cont >= 5:
      break
  print(f'\nSeus números apostados foram: {listaAposta}') 
  lista = list()
  cont = 0
  while True:
    num = randint(1, 60)
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 5:
      break
  print(f'Os número sorteados foram: {lista}')  
  igual = list()
  # Tanto as variaveis (v, valor, conteudo), são iguais, para acessar o valor de cada lista pelo for
  for posicao, conteudo in enumerate(listaAposta):
    for indice, valor in enumerate(lista):
      if conteudo == valor:
        igual.append(conteudo)
        for i, v in enumerate(igual):
          print('\nOs números acertados foram: ', end=' ')
          print(f'{v}')

  enter = input('\nPressione ENTER para prosseguir....')


while True:
  replit.clear()
  menu()
  opcao = int(input('Selecione uma opção: '))
  if opcao == 1:
    percorrerString()
  elif opcao == 2:
    jogoQuina()
  elif opcao == 9:
    print('\nPrograma Finalizado.... ')  
    break
