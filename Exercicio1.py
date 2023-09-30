print('Bem vindo a loja do Gustavo!') #Identificador pessoal
valor = float(input('Entre com o valor desejado: ')) #Entrada do valor
quantidade = int(input('Entre com a quantidade desejada: ')) #Entrada da quantidade
desconto = 0

if quantidade <= 9:
  desconto = 0
elif quantidade >= 10 and quantidade <= 99:
  desconto = 0.05
elif quantidade >= 100 and quantidade <= 999:
  desconto = 0.10
else:
  desconto = 0.15

total_sem_desconto = valor * quantidade
print('O valor total sem desconto é de: R$ {:.2f}'.format(total_sem_desconto)) #Valor sem desconto
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto
print('O valor com desconto é de: R$ {:.2f}'.format(total_com_desconto)) #Valor com desconto
