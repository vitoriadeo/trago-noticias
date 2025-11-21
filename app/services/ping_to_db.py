import requests
import os, logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "apikey": key
}


def keep_db_alive():
    try:
        response = requests.head(url, headers=headers, timeout=10)
        logger.debug(f"resp: {response.status_code}")

    except requests.exceptions.ConnectionError as e:
        logger.error(f"Erro de conexão: {e}")
        raise e
    except requests.exceptions.Timeout as e:
        logger.error(f"Erro de Timeout: {e}")
        raise e
    except Exception as e:
        logger.error(f"Erro: {e}")
        raise e
