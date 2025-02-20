import pytest
from ingestao.ingestao_dados import ingestao_clientes

def test_ingestao_clientes():
    dados = [
        {'nome': 'Renan', 'email': 'renan@example.com'},
        {'nome': 'Afonso', 'email': 'afonso@example.com'}
    ]
    clientes = ingestao_clientes(dados)
    assert isinstance(clientes, list) and len(clientes) == 2
