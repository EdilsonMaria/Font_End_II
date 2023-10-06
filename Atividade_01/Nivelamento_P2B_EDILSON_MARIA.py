# Nivelamento P2B - Front End II - EDILSON MARIA (17/08/2023)

# Declaração de variáveis e listas
nomes = []
alturas = []
generos = []
soma_altura_homens = 0
qtd_homens = 0
qtd_mulheres = 0

# Coleta de informações
for i in range(0,3):
    nome = input("Digite seu nome: ")
    nomes.append(nome)
    print(f"Olá sr.(a) {nome}, responda as seguintes perguntas por favor!")
    print()
    altura = float(input("Digite sua altura: "))
    alturas.append(altura)
    genero = input("Digite seu gênero F (para Feminino) ou M (para Masculino)): ").upper()
    generos.append(genero)

    print()

# Condições estabelecidas para maior e menor altura, média dos homens e quantidade de mulheres
maior_altura = -1
nome_maior_altura = ""
menor_altura = float("inf")
nome_menor_altura = ""

for i in range(0,3):
    if alturas[i] > maior_altura:
        maior_altura = alturas[i]
        nome_maior_altura = nomes[i]

    if alturas[i] < menor_altura:
        menor_altura = alturas[i]
        nome_menor_altura = nomes[i]

    if generos[i] == "M":
        soma_altura_homens += alturas[i]
        qtd_homens += 1
        media_altura_homens = soma_altura_homens / qtd_homens

    if generos[i] == "F":
        qtd_mulheres += 1

# Exibe a maior e menor altura
print("Dados solicitados:")
print(f"A maior altura é de {nome_maior_altura} com {maior_altura:.2f} m, e a menor altura é de {nome_menor_altura} com {menor_altura:.2f} m")

# Média da altura dos homens
if qtd_homens > 0:
    print(f"A média da altura dos homens é {media_altura_homens:.2f} m")
else:
    print("Nenhum homem foi inserido para o cálculo da média das alturas")

# Exibe a quantidade de mulheres
print(f"Foram informadas {qtd_mulheres} mulheres")
