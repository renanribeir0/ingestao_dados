import pytest
from ingestao.ingestao_dados import ingestao_clientes

def test_ingestao_clientes():
    dados = [
        {'nome': 'João', 'email': 'joao@example.com'},
        {'nome': 'Maria', 'email': 'maria@example.com'}
    ]
    clientes = ingestao_clientes(dados)
    # Espera que dois clientes tenham sido inseridos
    assert isinstance(clientes, list) and len(clientes) == 2
