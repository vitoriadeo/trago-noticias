# Apenas inicialização e execução do servidor
# É o arquivo que inicia minha aplicação Flask.

from dotenv import load_dotenv

load_dotenv()

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)