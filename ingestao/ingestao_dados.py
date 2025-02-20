print("Iniciando ingestao_dados.py...")

from ingestao.supabase_client import inserir_cliente

def ingestao_clientes(dados_clientes: list) -> list:
    """
    Função para orquestrar a ingestão de uma lista de clientes.
    
    Args:
        dados_clientes (list): Lista de dicionários, onde cada dicionário representa
                               um cliente com as chaves 'nome' e 'email'.
    
    Returns:
        list: Lista com os resultados da inserção de cada cliente.
    """
    clientes_inseridos = []
    for cliente in dados_clientes:
        try:
            nome = cliente.get('nome')
            email = cliente.get('email')
            resposta = inserir_cliente(nome, email)
            clientes_inseridos.append(resposta)
        except Exception as e:
            print(f"Erro ao inserir cliente {cliente}: {e}")
    return clientes_inseridos
