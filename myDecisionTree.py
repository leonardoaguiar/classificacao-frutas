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

def partition(rows, question):
    """Separação do conjunto de dados de exemplo.
    Para cada linha na tabela de exemplo, será verificado a resposta da pergunta.
    Se for verdadeira, então será adicionado a linha das verdadeiras. Do contrário,
    será adicionado a linha das falsas.
    """
    true_rows, false_rows = [], []
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


#######
# Exemplo de separação dos dados baseado na cor vermelha
# true_rows, false_rows = partition(training_data, Question(0, 'Vermelho'))
# Linhas que contém a cor vermelha.
# print("Linhas com vermelho: ", true_rows)
# Linhas que não contém cor vermelha.
# print("Linhas sem vermelho: ", false_rows)
#######

def gini(rows):
    """Calcula o Gini Impurity para a lista de linhas.
    See: https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity
    """
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity


#######
# Alguns exemplos de como o Gini Impurity funciona.
#
# Primeiro, vamos ver um conjunto de dados iguais.
# no_mixing = [['Maçã'], ['Maçã']]
# irá retornar 0.0
# print(gini(no_mixing))
#
# Agora, vamos ver um conjunto de dados 50:50 maçã:uva
# some_mixing = [['Apple'], ['Orange']]
# irá retornar 0.5 - indicando que existe uma chande de 50% de erro na
# classificação.
# print(gini(some_mixing))
#
# Agora, vamos ver um conjunto de dados com muitas características (labels)
# diferentes.
# lots_of_mixing = [['Maçã'],
#                   ['Laranja'],
#                   ['Uva'],
#                   ['Pera'],
#                   ['Banana']]
# irá retornar 0.8
# print(gini(lots_of_mixing))
#######

def info_gain(left, right, current_uncertainty):
    """Information Gain.
    A incerteza do nó inicial, subtraída da impureza ponderada (Gini Impurity)
    dos dois nós filhos.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)


#######
# Calculado a incerteza dos dados de treinamento
# current_uncertainty = gini(training_data)
# print("Incerteza dos dados de treinamento: ", current_uncertainty)
#
# Quanta informação podemos ganhar particionando os dados pela cor Verde?
# true_rows, false_rows = partition(training_data, Question(0, 'Verde'))
# learned = info_gain(true_rows, false_rows, current_uncertainty)
# print("Quantidade de aprendizado pela cor verde: ", learned)
#
# E se separarmos os dados pela cor vermelha?
# true_rows, false_rows = partition(training_data, Question(0, 'Vermelho'))
# learned = info_gain(true_rows, false_rows, current_uncertainty)
# print("Quantidade de aprendizado pela cor vermelha: ", learned)
#
# Parece que aprendemos mais usando a cor 'Vermelha' (0.37), do que a 'Verde' (0.14)
# Porque? Vamos ver uma separação de dados diferentes e ver qual fica mais
# embaralhada
# true_rows, false_rows = partition(training_data, Question(0, 'Vermelho'))
#
# Aqui, as linhas verdadeiras só contém 'Uvas'.
# print(true_rows)
#
# E nas linhas falsas contém dois tipos de frutas. Nada mal!
# print(false_rows)
#
# Por outro lado, separar os dados pela cor verde não ajudaria muito.
# true_rows, false_rows = partition(training_data, Question(0, 'Verde'))
#
# Nós isolamos uma maçã em uma linha verdadeira.
# print(true_rows)
#
# Mas, as linhas falas estão mal arranjadas.
# print(false_rows)
#######

def find_best_split(rows):
    """Encontra a melhor 'Question' para se fazer por iteração de cada
    característica / valor e calcula o ganho de informação (info_gain)."""
    best_gain = 0  # variável para armazenar o melhor ganho de informação.
    best_question = None
    current_uncertainty = gini(rows)
    n_features = len(rows[0]) - 1

    for col in range(n_features):

        # pega valores únicas nas colunas
        values = set([row[col] for row in rows])

        for val in values:

            question = Question(col, val)

            # separação dos dados
            true_rows, false_rows = partition(rows, question)

            # Pula esta separação de dados se ela não for divisivel.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calcula o ganho de informação para esta separação de dados
            gain = info_gain(true_rows, false_rows, current_uncertainty)

            if gain >= best_gain:
                best_gain, best_question = gain, question

    return best_gain, best_question


#######
# Encontrando a melhor pergunta a ser feita primeiro para o conjunto de dados.
# best_gain, best_question = find_best_split(training_data)
# print("Melhor ganho de informação: ", best_gain)
# print("Melhor pergunta: ", best_question)
#######

class Leaf:
    """Um nó (folha) de classificação de dados.
    Ele segura um dicionário de classes (Ex. "Maçã") pelo número de vezes que
    ele aparevce nas linhas do conjunto de dados que chegam a este nó (folha)
    """

    def __init__(self, rows):
        self.predictions = class_counts(rows)


class Decision_Node:
    """Um nó de decião, que faz as perguntas.
    Ele segura a referência para a pergunta e de duas nós filhos.
    """

    def __init__(self,
                 question,
                 true_branch,
                 false_branch):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch


def build_tree(rows):
    """Construtor da árvore.
    """

    # Tenta separar o conjunto de dados para cada atributo único,
    # calcula o ganho de informação e returna a pergunta que produzira o maior
    # ganho de informação.
    gain, question = find_best_split(rows)

    # Base: sem ganho de informações
    # Desde que não tenhamos mais perguntas,
    # retornaremos uma folha.
    if gain == 0:
        return Leaf(rows)

    # Se chegamos aqui, temos alguma característica (feature) útil para
    # nos ajudar a particionar os dados.
    true_rows, false_rows = partition(rows, question)

    # Recursivamente construindo a árvore com os valores verdadeiros
    true_branch = build_tree(true_rows)

    # Recursivamente construindo a árvore com os valores falsos
    false_branch = build_tree(false_rows)

    # Returna o nó com a questão.
    # Isto registrará a melhor característica para usar neste ponto,
    # assim como o ramo (branch) que deverá ser seguido dependendo da resposta
    return Decision_Node(question, true_branch, false_branch)
