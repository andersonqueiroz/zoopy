# Zoopy

Biblioteca desenvolvida para interfacear a comunicação com a API da [Zoop](https://docs.zoop.co/reference#introducao).

## Instalação
Adicionar o requirements.txt da aplicação:

    -e git+https://github.com/andersonqueiroz/zoopy.git#egg=zoopy

E executar pip install -r requirements.txt

## Utilização

Para utilizar a biblioteca, deve-se autenticar e depois utilizar os métodos desejados:

    from zoopy.utils import authentication_key
    from zoopy import buyer

    authentication_key(
	    api_key=config('ZOOP_API_KEY'),
	    marketplace_id=config('ZOOP_MARKETPLACE_ID')
    )

	buyers = buyer.list(params=<your data>)

## Desenvolvimento e testes

As dependências de desenvolvimento encontram-se no arquivo requirements-dev.txt

Para testar, deve-se renomear o arquivo **.env.TEMPLATE**, na raiz do projeto, para **.env** e especificar a API key e o ID do marketplace.

A execução dos testes se dá pelo comando:

    python -m unittest

Ou especificando o serviço:

    python -m unittest tests.test_buyer

   

