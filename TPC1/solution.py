def general_parser(file_path):
    file = open(file_path)

    organized_data = {}
    fields = file.readline().replace("\n", "").split(",")
    for i in range(len(fields)):
        organized_data[i] = []

    for line in file:
        line = line.replace("\n", "")
        data = line.split(",")
        for i, item in enumerate(data):
            organized_data[i].append(item)
        
    new_organized_data = {}
    for i, data_desc in enumerate(fields):
        new_organized_data[data_desc] = organized_data[i]
    organized_data = new_organized_data

    file.close()

    return organized_data

# Fazer parsing do ficheiro
organized_data = general_parser("Dados/emd.csv")

# Lista das modalidades ordenadas alfabeticamente
lista_ordenada_modalidades = sorted(organized_data["modalidade"])

# Percentagens de atletas aptos e inaptos para a prática desportiva
percentagem_aptos = organized_data["resultado"].count("true")
percentagem_inaptos = organized_data["resultado"].count("false")
total_atletas = percentagem_aptos + percentagem_inaptos
percentagem_aptos = round(percentagem_aptos * 100 / total_atletas, 2)
percentagem_inaptos = round(percentagem_inaptos * 100 / total_atletas, 2)

# Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
distribuicao_escaloes = {}
for idade in organized_data["idade"]:
    escalao = int(idade) // 5
    if escalao not in distribuicao_escaloes:
        distribuicao_escaloes[escalao] = 0
    distribuicao_escaloes[escalao] += 1

for atletas_escalao in distribuicao_escaloes.keys():
    distribuicao_escaloes[atletas_escalao] = round(distribuicao_escaloes[atletas_escalao] * 100 / total_atletas, 2)

new_distribuicao_escaloes = {}
for key, value in distribuicao_escaloes.items():
    escalao_string = "[" + str(key*5) + "-" + str(key*5 + 4) + "]"
    new_distribuicao_escaloes[escalao_string] = value

distribuicao_escaloes = new_distribuicao_escaloes

print("Lista das modalidades ordenadas alfabeticamente -> " + str(lista_ordenada_modalidades))
print("Percentagem atletas aptos -> " + str(percentagem_aptos))
print("Percentagem atletas inaptos -> " + str(percentagem_inaptos))
print("Distribuição dos atletas por escalões -> " + str(distribuicao_escaloes))