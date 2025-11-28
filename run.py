# Apenas inicialização e execução do servidor
# É o arquivo que inicia minha aplicação Flask.

from dotenv import load_dotenv

load_dotenv()

from app import create_app
import logging

logging.basicConfig(
    level=logging.INFO,
    encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('run.log'), logging.StreamHandler()]
)

logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("python_http_client").setLevel(logging.WARNING)
logging.getLogger("werkzeug").setLevel(logging.WARNING)

app = create_app()

if __name__ == "__main__":
    app.run()
