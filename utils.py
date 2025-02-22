def validar_dados_cliente(dados: dict) -> bool:
    """Valida se os dados do cliente estão corretos e não são vazios."""
    if 'nome' not in dados or not dados['nome'].strip():
        return False
    if 'email' not in dados or not dados['email'].strip():
        return False
    return True
