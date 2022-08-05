
print("--------------------------------------------")
print("       O PASSO A PASSO SUCO DE LARANJA      ")
print("--------------------------------------------")

nome = str(input(f"Olá, Qual O Seu Nome?:"))
print("Oi,", nome, "irei apresentar uma lista do material que precisa para o suco de Laranja:")

#  RESOLVER DEPOIS - voltei = str(f"Que ótimo que voltou", nome)

print("--------------------------------------------")

print("Lista do Material: \n4 = Laranjas\n1 = Espremedor\n1 = Peneira\n1 = Jarra\n* = Açucar a gosto\n* = Gelo a gosto")

print("--------------------------------------------")

lista_material = str(input(f"Tem todos os materias da lista, [Sim ou Não?]:"))
if lista_material == str("sim"):
    print(f"Então vamos iniciar o preparo")
else:
    print(f"Melhor ir comprar oque falta")
    print(f"Até Breve!")

print("--------------------------------------------")
print(f"Preste muito atenção no processo!")
print(f"Então vamos ao preparo!")
print("--------------------------------------------")


# Cortando e espremendo
print("--------------------------------------------")
print(f"Pegue as laranjas, lave e corte em bandas")
print(f"Pegue o espremedor")
print(f"Pressione uma banda da laranaja,")
print(f"Gire no sentido horario até extrar o suco")
print("--------------------------------------------")

# Peneirando opcionais
print(f"Pegue a jarra da sua preferencia")
print(f"Coloque a peneira posicionada na jarra,")
print(f"Vai despejando o suco da laranja, até terminar")
print(f"Caso ultrapasse a quantidade limite,")
print(f"Utilize outra jarra ou pare de despejar")
print("--------------------------------------------")

# Gelo e açucar
print(f"*Caso deseje açucar, acrescente a gosto,")
print(f"*Também podendo deixar bem gelado com gelo a gosto")
print("--------------------------------------------")
print(f"Agora é só apreciar seu suco de laranja!")

exit("-----------------OBRIGADO-------------------")
