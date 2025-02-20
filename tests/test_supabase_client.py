import pytest
from ingestao.supabase_client import inserir_cliente
from ingestao.exceptions import SupabaseError

def test_inserir_cliente():
    # Testa a inserção de um cliente válido
    response = inserir_cliente('João', 'joao@example.com')
    assert response is not None
    # Verifica se a resposta contém dados inseridos
    assert isinstance(response, list) and len(response) > 0

def test_inserir_cliente_com_erro():
    # Testa a inserção com dados inválidos, esperando que levante uma exceção
    with pytest.raises(SupabaseError):
        inserir_cliente('', '')
