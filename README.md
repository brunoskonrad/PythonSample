# PythonSample
Exemplos de Python para uma introdução. Em construção

### Exemplos gerais

Dentro de *sample/general.py* estão exemplos em geral sobre Python.

Para rodá-los no terminal, escreva na raiz do projeto:

``` bash
$ python sample/general.py
```

### Pacotes e Módulos

A estrutura de diretórios do projeto está definindo **dois** pacotes: *sample* e *test*;

O que define um **pacote** é um diretório que contenha o arquivo **__init__.py** em sua raiz. O restante são os **módulos** do pacote.

Por exemplo, para importar o módulo *flow_control_sample* do **sample** é preciso escrever em um arquivo python:


``` python
from sample import flow_control_sample

flow_control_sample.basic_if(20)
```

Pode-se ainda importar apenas uma função ou classe de um módulo

``` python
from sample.flow_control_sample import basic_if

basic_if(20)
```

### Testar

No seu terminal, na raiz do projeto, executar o comando para testar.

``` bash
$ python -m unittest test
```
