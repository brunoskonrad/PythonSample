# -*- coding: utf-8 -*-

# Define uma função que recebe uma lista de parâmetros e retorna a multiplicação de todos os valores.
# usando laço for, para exemplificar como 'é feito em outras linguagens'
def multiplicar(*args):
    total = 0 if len(args) == 0 else 1
    for i in args:
        total *= i
    return total


# Define uma função que recebe uma lista de parâmetros e retorna a multiplicação de todos os valores.
# usando a função reduce, de programação funcional, para trabalhar com a lista
def multi(*args):
    return reduce(lambda x, y: x * y, args) if len(args) > 0 else 0


# chamando as funções declaradas acima
a = [1, 2, 3, 4]
print(multiplicar(*a)) # 24
print(multi(*a)) # 24


# declaração de uma função com parâmetros default.
def somar(x=0, y=0):
    print x + y

# exemplos de chamadas da função somar, declarada acima
somar() # 0
somar(1) # 1
somar(1, 2) # 3

# aqui é um exemplo omitindo o primeiro parâmetro e passando apeans o último.
somar(y=2) # 2

# e aqui está sendo passado um dictionary, antecedido por dois asteriscso, como parâmetro.
# A key deve ser a mesma do nome da declaração da função.
somar(**{'y': 2})


# itera os items do dictionary e escreve sua chave e valor.
dictionary = {'Python': 'é', 'afudê?': True}
for key, value in dictionary.items():
    print key, value


# itera uma lista de 0 até 10 e escreve o seu valor
for i in range(10):
    print(i)


# itera, usando o while, de 0 até 10. Escreve o seu valor a cada iteração.
i = 0
while i < 10:
    print(i)
    i += 1


class Usuario(object):
    """
    Essas três aspas representam a 'documentação'. O que estiver abaixo de uma classe ou função é a documentação da mesma; chamada de
    docstring.

    Python possui herança múltipla, então pode-se passar mais de uma classe como parâmetro na hora de definir uma nova.
    Lembrando que uma das boas práticas de Orientação a Objetos é a de composição (horizontal) sobre a herança (verical)
    """

    def __init__(self, nome='Bruno'):
        """
        O construtor de uma classe é o método __init__(self). O self seria o 'this' do Java, por exemplo. Deve ser explícito como o
        primeiro parâmetro de todo método de objeto.
        """
        self.nome = nome

    @property
    def autorizado(self):
        """
        O @property é uma anotação que diz que esta função é, na realidade, uma propriedade do objeto. Aqui pode-se fazer uma validação
        mais complexa e que varia de acordo com o estado do objeto. Nesse caso é apenas para exemplificar, então o retorno é sempre True.
        """
        return True

    def __str__(self):
        """
        Aqui temos a sobrescrita de um método da classe pai - object -; esse método é chamado quando precisa obter a string do objeto.
        """
        return '{0} está autorizado? {1}'.format(self.nome, self.autorizado)

# instanciando um objeto Usuario sem passar o nome.
bruno = Usuario()
print (bruno) # Bruno está atualizado? True
