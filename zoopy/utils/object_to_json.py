import json
from future.utils import integer_types


class ObjectJSON(object):
    def to_json(self):
        dicionary = json.loads(json.dumps(self, default=lambda o: o.__dict__))
        return json.dumps(dicionary)


def process_name_key(dictionary):
    if not isinstance(dictionary, dict):
        return dictionary

    new_dictionary = {}

    for key in dictionary:
        new_dictionary[key] = process_name_key(dictionary[key])

    return new_dictionary


def remove_none(data):
    if isinstance(data, dict):
        return remove_none_dict(data)
    elif isinstance(data, list):
        return remove_none_list(data)

    return data

def remove_none_dict(obj):
    retorno = {}
    for chave in obj:
        valor = obj[chave]
        types = integer_types + (float, complex)

        if (valor or isinstance(valor, types)):
            if valor:
                retorno[chave] = remove_none(valor)
        
    return retorno

def remove_none_list(lista):
    resposta = []
    for linha in lista:
        valor = remove_none(linha)
        resposta.append(valor)

    return resposta