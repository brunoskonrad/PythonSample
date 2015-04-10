# -*- coding: utf-8 -*-
# Esse arquivo de exemplos é seguindo o tutorial oficial encontrado em: https://docs.python.org/2/tutorial/controlflow.html

# A mensagem de sucesso. É repetido, então vem pra cá!
MESSAGE = 'Sucesso, gente'

# Exemplo básico do uso da condicional IF
def basic_if(value, check=20, message=MESSAGE, fail=None):
    if value == check:
        return message
    else:
        return fail


# Exemplo para verificar se um valor está dentro de uma lista ou dicionário
def value_in_if(list, value, message=MESSAGE, fail=None):
    if value in list:
        return message
    else:
        return fail


# Exemplo básico de FOR onde recebe uma função que será executada a cada iteração
# de 1 até o total.
def basic_for(total, fn):
    val = 0
    for i in range(1, total):
        val = fn(i, val)
    return val


# Exemplo com um FOR onde é passada uma função para dizer se será chamado o
# comando CONTINUE para pular uma das chamadas de fn
def basic_for_continue(total, fn, continue_at=None):
    val = 0
    for i in range(1, total):
        if continue_at is not None and continue_at(i): continue
        val = fn(i, val)
    return val


# Só diz que não tem nada no corpo da função
def basic_pass():
    pass


# Exemplo usando *args, que é a inserção de parâmetros da forma function(1, 2, 3, 4) e, o objeto args,
# é uma tuple com os parâmetors passados.
def basic_function_args(*args):
    return args


# Parecido com o exemplo anterior usando *args, porém o **kwargs trabalha com Dictionary e os parâmetros
# são noemados, exemplo: function(nome='Bruno Konrad', idade=21)
def basic_function_kwargs(**kwargs):
    return kwargs
