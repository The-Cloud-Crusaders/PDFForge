from app import create_app
from config import AppConfig
if __name__ == "__main__":
    app = create_app(AppConfig)
    app.run(debug=True, host="0.0.0.0")
