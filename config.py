from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Agora pega a chave da variável de ambiente
API_KEY = os.getenv("API_KEY")

# Usa a chave normalmente
url = "https://api.themoviedb.org/3/movie/"

print(url)