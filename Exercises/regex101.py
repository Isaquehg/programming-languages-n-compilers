'''Principais métodos
FINDALL("padrão", txt) -> Retorna uma lista
SEARCH("Padrão", txt) -> Retorna True/False
SPLIT("padrão", txt, num_ocorrencias) -> retorna o texto com split
SUB("padrão", "padrão a substituir", txt) -> retorna o text substituido
'''

import re


# SEARCH
print("---------------SEARCH---------------")
txt1 = "Os melhores engenheiros são do Brasil"

# Colocar entre ^ $
# .* significa qualquer combinação de quaisquer caracteres
x = re.search("^Os.*Brasil$", txt1)

if x:
    print("Padrão encontrado!!")
else:
    print("Padrão não encontrado")

# group e span
txt2 = "o rato roeu a roupa do rei de roma. Que rato malvado!"

# Obs.: Não usamos ^$ pois estamos obtendo apenas parte do texto, não ele inteiro, como no search
y = re.search('r[a-z]*o', txt2)

# Apenas a primeira aparição
print("1) Primeira Aparição")
if y:
    print("Padrão 2 encontrado!!")
    print("Encontrado na palavra:", y.group())
else:
    print("Padrão não encontrado")

# Todas aparições
print("2) Todas Aparições")
for match in re.finditer('r[a-z]+o', txt2):
    print("Palavra com padrão encontrado: ", match.group())
    print("Indexes inicial e final da palavra encontrada: ", match.span())

# FINDALL
print("---------------FINDALL---------------")
txt3 = "oi! teu pai tem boi? Foi o que pensei"

x = re.findall("oi", txt3)
print("Matches: ", x)
print("Quantidade:", len(x))


# SPLIT
print("---------------SPLIT---------------")
txt4 = "Teste teste Teste teste Teste"
w = re.split("\ ", txt4)
print(w)

# SUB
print("---------------SUB---------------")
txt5 = "Quando chover, busque pelo arco-íris. Quando encontrar, saia correndo dele"

z = re.sub("Quando", "Sempre que", txt5)
print(z)