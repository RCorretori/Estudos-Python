"""
Recebendo dados do usuario

"""
#Entrada de dados
print("Qual o seu nome: ")
nome = input() #input -> Entrada

#Forma antiga 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Forma moderna 3.x
#print('Seja bem vindo(a) {0}' .format(nome))

#Forma atual 3.7+
print(f'Seja bem-vindo(a)')

print("Qual sua idade: ")
idade = input()

#Processamento


#Saída
#Forma antiga 2.x
#print('O %s tem %s anos' % (nome, idade)) #Caso só tenha uma variavel não colocar "()" mas caso tenha mais de uma, colocar

#Forma moderna 3.x
#print('O(A) tem {0} tem {1} anos' .format(nome, idade))





