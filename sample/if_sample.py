# -*- coding: utf-8 -*-

MESSAGE = 'Sucesso, gente'

# Exemplo básico do uso da condicional IF
def basic(value, check=20, message=MESSAGE, fail=None):
    if value == check:
        return message
    else:
        return fail


# Exemplo para verificar se um valor está dentro de uma lista ou dicionário
def value_in(list, value, message=MESSAGE, fail=None):
    if value in list:
        return message
    else:
        return fail
