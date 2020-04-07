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

def is_numeric(value):
    """Verifica se o valor é numérico."""
    return isinstance(value, int) or isinstance(value, float)


#######
# print(is_numeric(7))
# print(is_numeric("Red"))
#######

class Question:
    """A classe 'Question' será usada para particionar os dados de exemplo.
    Esta classe só armazenará 'o número da coluna' (Ex. 0 para Cor) e o 
    'valor da colona' (Ex. Verde). O método 'match' será usado para comparar
    o valor da característica (feature) no exemplo com o valor da característica
    armazenado na 'Question'.
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def match(self, example):
        # compara o valor da característica (feature) no exemplo com o valor
        # da característica armazenado na 'Question'
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # Imprime a pergunda de maneira legivel e amigavel para humanos.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "%s %s %s?" % (
            header[self.column], condition, str(self.value))


#######
# Exemplo de pergunta numérica
# print(Question(1, 3))
# Exemplo de pergunda de características
# q = Question(0, 'Verde')
# print(q)
# Exemplo usados os dados de teste.
# example = training_data[0]
# ... verficando a resposta
# print(q.match(example))
#######
