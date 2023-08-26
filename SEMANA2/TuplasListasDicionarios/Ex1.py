for aluno in range(quantidadaAluno):
    listaNotas.append([])
    for nota in range(quantidadeNotas):
        listaNotas[aluno].append(
            float(
                input(f"Digite a nota {nota+1} do aluno {aluno+1}: ")
            )
        )
for notas in listaNotas:
    listaMedias.append(
        sum(notas) / len(notas)
    )

alunos_aprovados = sum(1 for media in listaMedias if media >= 7.0)

print(f"Número de alunos com média maior ou igual a 7.0: "(alunos_aprovados))