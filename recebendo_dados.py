"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:

-Aspas simples;
-Aspas duplas;
-Aspas simples triplas;
-Aspas duplas triplas;

Exemplos:
-Aspas simples -> 'Rafael'
-Aspas duplas -> "Rafael"
-Aspas simples triplas -> '''Rafael'''
"""
#-Aspas duplas triplas -> """Rafael"""

#Entrada de dados
#print("Qual o seu nome: ")
#nome = input() #input -> Entrada

nome = input('Qual seu nome? ')

#Forma antiga 2.x
#print('Seja bem-vindo(a) %s' % nome)

#Forma moderna 3.x
#print('Seja bem vindo(a) {0}' .format(nome))

#Forma atual 3.7+
print(f'Seja bem-vindo(a) {nome}')

#print("Qual sua idade: ")
#idade = input()

idade = int(input('Qual a sua idade? '))

#Processamento


#Saída
#Forma antiga 2.x
#print('O %s tem %s anos' % (nome, idade)) #Caso só tenha uma variavel não colocar "()" mas caso tenha mais de uma, colocar

#Forma moderna 3.x
#print('O(A) tem {0} tem {1} anos' .format(nome, idade))

#Forma atual 3.7+
print(f'A {nome} tem {idade} anos')

#int(idade) -> cast
#Cast é a 'conversão' de um tipo de dado para outro

print(f'O(A) {nome} nasceu em {2021 - idade}')





