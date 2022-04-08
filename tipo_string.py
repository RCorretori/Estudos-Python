#Em python um dado considerado do tipo string é quando está com '', "", ''' ''', """ """

nome = 'Rafael'
print(nome)
print(type(nome))


nome = "Gustavo"
print(nome)
print(type(nome))

nome = '''Renato'''
print(nome)
print(type(nome))

nome = """Juan"""
print(nome)
print(type(nome))

#Para letra maiuscula
nome = 'Ronaldo'
print(nome.upper())

#Para letra minúscula
nome = 'NEYMAR'
print(nome.lower())

#Para listar a string
nome = 'Lionel Messi'
print(nome.split())

#Para imprimir apenas uma palavra ou apenas uma parte dela
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[C, a, r, l, o, s, A, l, b, e, r, t, o]

"""

nome = 'Carlos Alberto'
print(nome[0:6]) #Slice de string

nome = 'Carlos Alberto'
print(nome[7:14]) #Slice de string

#[     0,       1]
#['Carlos', 'Alberto']
print(nome.split()[0])
print(nome.split()[1])

print(nome[7], nome[10]) 

print(nome[::-1]) #Inverte a string

print(nome.replace('r', 'A')) #Substitui a String escolhida

texto = 'Nós todos somos amigos de infância'
print(texto)
print(texto[::-1])
