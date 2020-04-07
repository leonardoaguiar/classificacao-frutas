# Tabela com dados de exemplo.
# Formato: cada linha é um exemplo.
# A última coluna é o label (rótulo).
# As duas primeiras colunas são as características (features)..

training_data = [
    ['Verde', 3, 'Maçã'],
    ['Amarelo', 3, 'Maçã'],
    ['Vermelho', 1, 'Uva'],
    ['Vermelho', 1, 'Uva'],
    ['Amarelo', 3, 'Limão'],
]

# Nome das colunas.
# somente para exibir a árvore.
header = ["cor", "diâmetro", "fruta"]


def unique_vals(rows, col):
    """Encontra um valor único em cada coluna na tabela de exemplos."""
    return set([row[col] for row in rows])


#######
# print(unique_vals(training_data, 0)) # identifica os valores da primeira coluna
# print(unique_vals(training_data, 1)) # identifica os valores da segunda coluna
#######

def class_counts(rows):
    """Conta a quantidade de cada tipo de fruta na tabela de exemplo"""
    counts = {}  # dicionário de frutas (labels) -> quantidade.
    for row in rows:
        # na tabel deste exemplo, a fruta (label) será sempre a última coluna
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


#######
# print(class_counts(training_data))
#######
