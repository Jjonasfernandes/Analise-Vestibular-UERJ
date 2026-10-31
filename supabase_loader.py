import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import create_client


def conectar_supabase():

    caminho_env = Path(__file__).resolve().parent / ".env"
    load_dotenv(caminho_env)

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError(
            "Credenciais do Supabase não encontradas no arquivo .env"
        )

    supabase = create_client(url, key)

    return supabase