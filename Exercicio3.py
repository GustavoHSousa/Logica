def dimensoesObjeto(): #Inicio função objetos
  while True:
    try:
      altura = float(input("Informe a altura do Objeto (em cm): ")) #Valor da altura objeto
      largura = float(input("Informe a largura do Objeto (em cm): ")) #Valor da largua objeto
      comprimento = float(input("Informe o comprimento do Objeto (em cm): ")) #Valor do comprimento do objeto
      volume = altura*largura*comprimento #Calculo do volume
      print('O volume do objeto é (em cm³): {}'.format(volume))
      if volume < 1000:
        return 10.00
      elif 1000 <= volume < 10000:
          return 20.00
      elif 10000 <= volume < 30000:
            return 30.00
      elif 30000 <= volume < 100000:
            return 50.00
      elif volume >= 100000:
            print('Está dimensão não é aceita. Tente novamente.')
            continue
    except ValueError:
        print('Você digitou um valor não numérico. Tente novamente.')
        continue #Volta para o inicio da laço

#Fim função objetos

def pesoObjeto(): #Inicio função peso
  while True:
    try:
      peso_objeto = float(input('Entre com o peso do Objeto (em kg): '))
      if peso_objeto < 0.1: #Compara o peso
        return 1.0
      elif 0.1 <= peso_objeto < 1:
        return 1.5
      elif 1 <= peso_objeto < 10:
          return 2.0
      elif 10 <= peso_objeto < 30:
          return 3.0
      elif peso_objeto > 30:
          print('Objeto muito pesado. Tente novamente') #Peso acima do permitido
          continue #Volta para o inicio da laço
    except ValueError:
            print('Você digitou um valor não numérico. Tente novamente.') #Tratamento de erro
            continue #Volta para o inicio da laço

#Fim função peso

def rotaObjeto():   #Funçao rotas
    while True:
        print('Selecione a rota:')
        print(' RS - Rio de Janeiro x São Paulo')
        print(' SR - São Paulo x Rio de Janeiro')
        print(' BS - Brasília x São Paulo')
        print(' BR - Brasilia x Rio de Janeiro')
        print(' RB - Rio de Janeito x Brasilia')
        rotaObj = input('>>')
        if rotaObj == 'RS':
            return 1
        elif rotaObj == 'SR':
            return 1
        elif rotaObj == 'BS':
            return 1.2
        elif rotaObj == 'SB':
            return 1.2
        elif rotaObj == 'BR':
            return 1.5
        elif rotaObj == 'RB':
            return 1.5
        else:
            print('Essa rota não existe. Tente novamente.')
            continue #Volta para o inicio da laço

#Fim função rotas

#Inicio da main
print('Bem vindo a Transportadora de Gustavo Henrique de Sousa!') #Identificador pessoal
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensoes*peso*rota

print('Total ficou: R$ {:.2f} (Dimensões: {} * Peso: {} * Rota: {})'.format(total,dimensoes,peso,rota)) #Valor final
