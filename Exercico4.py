listaPecas = [] #Variável Global

#inicio cadastrar peças

def cadastrarPeca(codigo): # Função que cadastra peças
  print('Você selecionou a opção de Cadastrar Peça')
  print('O código da peça é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome da peça:')
  fabricante = input('Entre com o fabricante da peça:')
  valor = float(input('Entre com o valor R$ da peça:'))
  dicionarioPecas = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  listaPecas.append(dicionarioPecas.copy())

#fim cadastrar peças

#inicio consultar peças

def consultarPeca(): # Função que consulta peças

  while True:
    try:
      print('Você selecionou a opção de Consultar Peças ')
      opcaoConsultar = int(input('\nEscolha a opção desejada: \n'+
                            '1- Consultar Todas as peças\n'+
                            '2- Consultar peças por código\n'+
                           '3- Consultar peças por fabricante\n'+
                            '4- Retornar \n'+
                            '>>'))
      if opcaoConsultar == 1:
        print('Você Selecionou Consultar Todas as peças')
        for pecas in listaPecas: #varrer lista pecas
            print('-' * 20)
            for key, value in pecas.items(): #varrer chave e valor do dicionario pecas
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opcaoConsultar == 2:
        print('Você Selecionou Consultar Peças por Código')
        valorDesejado = int(input('Digite o Código: '))
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['codigo'] == valorDesejado): #o valor de código é igual valor desejado
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opcaoConsultar == 3:
        print('Você Selecionou a Consultar Peças por Fabricante')
        valorDesejado = input('Digite o Fabricante: ')
        print('-' * 20)
        for pecas in listaPecas:
          if(pecas['fabricante'] == valorDesejado):
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif opcaoConsultar == 4:
        return #vai para a main
      else:
        print('Opção inválida. Tente novamente')
        continue #Volta para o inicio do laço
    except ValueError:  #Caso digite uma letra
      print('Digite somente o que é pedido')
      continue #Volta para o inicio do laço

#fim consultar peças

#inicio remover peças

def removerPeca(): # Função que remove peças
    print('Você selecionou a opção de Remover Peças')
    valorDesejado = int(input('Entre com o código da peça que deseja remover: '))
    for pecas in listaPecas:
      if(pecas['codigo'] == valorDesejado):
        listaPecas.remove(pecas)
    else:
      print('Código removido.')
#fim remover peças

#inicio da main

print('Bem-vindo ao Controle de Estoque de Gustavo Henrique de Sousa')  #Identificador pessoal

registroPecas = 0

while True:
    try:
      opcao = int(input('\nEscolha a opção desejada: \n'+
                            '1- Cadastrar  peça\n'+
                            '2- Consultar peça\n'+
                            '3- Remover peça\n'+
                            '4- Sair \n'+
                            '>>'))
      if opcao == 1:
        registroPecas = registroPecas + 1
        cadastrarPeca(registroPecas)
      elif opcao == 2:
        consultarPeca()
      elif opcao == 3:
        removerPeca()
      elif opcao == 4:
        break #Fim do laço
      else:
        print('Opção inválida. Tente novamente')
        continue #Retorna ao inicio do laço
    except ValueError:
        print('Digite somente o que é pedido')

#Fim da main
