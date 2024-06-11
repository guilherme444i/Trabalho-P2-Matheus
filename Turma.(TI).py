alunos_turma = []

while True:
    aluno = input("Digite o nome do aluno (ou digite 'fim' para terminar): ")
    if aluno.lower() == 'fim':
        break
    alunos_turma.append(aluno)

print("Lista de alunos da turma:")
for aluno in alunos_turma:
    print(aluno)