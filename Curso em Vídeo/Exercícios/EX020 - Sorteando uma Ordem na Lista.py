#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome de outro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)