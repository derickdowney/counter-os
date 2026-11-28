from flask import Flask

flask_app = Flask(__name__)


@flask_app.get("/health")
def health_check():
    return {"status": "healthy"}
