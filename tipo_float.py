#Errado
valor = 1,44
print(valor)
print(type(valor))

#Certo
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2)) 

#Podemos converter um float para um int
"""
Ao converter valores float para inteiros, nós perdemos precisão

"""
res = int(valor)
print(res)
print(type(res))

#Podemos trabalhar com numeros complexos
variavel = 5j
