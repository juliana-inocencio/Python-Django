respostas_positivas = 0

perguntas=[
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
]

for perguntas in perguntas:
    resposta = input(pergunta +"(SIM/NÃO): ").lower
    if resposta == "SIM":
        respostas_positivas +=1

if respostas_positivas == 5:
    classificacao = "Assassino"
elif respostas_positivas >= 3:
    classificacao = "Cúmplice"
if respostas_positivas >= 2:
    classificacao = "Suspeito"
else:
    classificacao = "Inocente"