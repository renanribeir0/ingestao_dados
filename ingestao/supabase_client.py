import os
from supabase import create_client, Client
from dotenv import load_dotenv
from ingestao.utils import validar_dados_cliente
from ingestao.exceptions import SupabaseError

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_supabase_client() -> Client:
    url = os.getenv('SUPABASE_URL')
    api_key = os.getenv('SUPABASE_API_KEY')
    return create_client(url, api_key)

def inserir_cliente(nome: str, email: str) -> dict:
    # Valida os dados antes de inserir
    if not validar_dados_cliente({'nome': nome, 'email': email}):
        raise SupabaseError("Dados inválidos para o cliente")
    
    supabase = get_supabase_client()
    try:
        response = supabase.table('cliente').insert({
            'nome': nome,
            'email': email
        }).execute()
        return response.data
    except Exception as e:
        raise SupabaseError(f"Erro ao inserir cliente: {e}")
