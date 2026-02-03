"""Local development entry point for snow-flask-whoami."""
import dotenv
import waitress

from snow_flask_core import create_app
from snow_flask_core.logging_config import setup_logging

dotenv.load_dotenv()
setup_logging()

app = create_app()

if __name__ == "__main__":
    waitress.serve(app, listen='0.0.0.0:8000')
