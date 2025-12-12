from src.app import init_app
import os
import sys
from dotenv import load_dotenv
from waitress import serve
from wsgicors import CORS

load_dotenv()
sys.path.append(os.getcwd())


def main():
    port = int(os.getenv('APP_PORT', 6543))
    db_url = os.getenv('DB_URL')

    if not db_url:
        print("Error: DB_URL not found in .env file.")
        return

    settings = {
        'sqlalchemy.url': db_url
    }

    try:
        app = init_app(settings)
        app = CORS(app, headers="*", methods="*", origin="*", maxage="180")

        print(f"Server running on http://0.0.0.0:{port}")
        serve(app, host='0.0.0.0', port=port)

    except Exception as e:
        print(f"Failed to start: {e}")


if __name__ == '__main__':
    main()
