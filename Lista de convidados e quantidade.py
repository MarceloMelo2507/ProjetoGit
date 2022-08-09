
# Faça um programa que leia a quantidade de pessoas que serão convidadas para a festa.
# Apois isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
# Apois isso imprimir todos os nomes da lista.

print("\n--------------------------------------------------------------")
print("-------------LISTA DE CONVIDADOS DA GRANDE FESTA--------------")
print("--------------------------------------------------------------\n")

# SOLICITAÇÃO DE QUANTIDADE DE CONVIDADOS:
contador = 0
quantidade = int(input("Quantos Convidados Serão?:\n"))
nomes = []

# SOLICITAÇÃO DE NOMES DE CONVIDADOS:
for contador in range(quantidade):
    nome = (input("Quais os Nomes dos Convidados?:\n"))
    nomes.append(nome)
    contador += 1

    # RESULTADO DA LISTA DE CONVIDADOS
    print(f"\n{quantidade}", "Pessoas Foram Convidadas, e Elas São:\n")
    print(f"\n{nome}\n")

    # FIM DA LISTA DE CONVIDADOS
    print("--------------------------------------------------------------")
    print("---------------AGUARDAMOS VOCÊS A GRANDE FESTA----------------")
    print("--------------------------------------------------------------")
    break
