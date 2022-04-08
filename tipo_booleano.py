"""
True -> Verdadeiro
False -> Falso

Obs: Sempre inicia com letra minúscula

Errado:
true, false

Correto:
True, False

"""

#Negação (not):

ativo = True
print(ativo)
#Negando que esta falso
print(not ativo)

logado = False

#Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro. 
True or True -> True
True or False -> True
False or True -> True
False or False -> True

"""

print(ativo or logado)

#E (and):
"""
É uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro. 
True or True -> True
True or False -> False
False or True -> False
False or False -> False

"""
print(ativo and logado)


