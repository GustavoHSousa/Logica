print('Bem vindo a Lanchonete Gustavo Henrique de Sousa') #Identificador pessoaç
print('-------------------Cardápio--------------------') #Menu
print('| Código  |       Descrição        | Valor R$ |')
print('|  100    |  Cachorro-quente       |  9,00    |')
print('|  101    |  Cachorro-quente Duplo |  11,00   |')
print('|  102    |  X-Egg                 |  12,00   |')
print('|  103    |  X-Salada              |  13,00   |')
print('|  104    |  X-Bacon               |  14,00   |')
print('|  105    |  X-Tudo                |  17,00   |')
print('|  200    |  Refrigerante Lata     |   5,00   |')
print('|  201    |  Chá Gelado            |   4,00   |')
total = 0
while True:
  cod = input('Informe o código desejado: ') #Cogido do produto
  if cod == '100':
        total += 9  #Soma com o valores pedidos
        print('Você escolheu um Cachorro-quente de R$ 9,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '101':
        total += 11 #Soma com os valores pedidos
        print('Você escolheu um Cachorro-quente Duplo de R$ 11,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '102':
        total += 12 #Soma com os valores pedidos
        print('Você escolheu um X-Egg de R$ 12,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '103':
        total += 13 #Soma com os valores pedidos
        print('Você escolheu um X-Salada de R$ 13,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '104':
        total += 14 #Soma com os valores pedidos
        print('Você escolheu um X-Bacon de R$ 14,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '105':
        total += 17 #Soma com os valores pedidos
        print('Você escolheu um X-Tudo de R$ 17,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '200':
        total += 5 #Soma com o valores pedidos
        print('Você escolheu um Refrigerante Lata de R$ 5,00.Valor atual: R$ {:.2f}'.format(total))
  elif cod == '201':
        total += 4 #Soma com os valores pedidos
        print('Você escolheu um Chá Gelado de R$ 04,00.Valor atual: R$ {:.2f}'.format(total))
  else:
        print('Opção inválida') #Opção invalida
        continue #Volta para o inicio do laço
  Algo_mais = int(input ('Deseja pedir algo mais? \n 1 - Sim \n 0 - Não \n')) #Adicionar mais um item
  if Algo_mais == 1:
        continue #Volta para o incio do laço
  else:
    print('Total a pagar é: R$ {:.2f}'. format(total)) #Valor final
    break
