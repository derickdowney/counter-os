from flask import Blueprint

bp = Blueprint("counter", __name__)


@bp.get("/health")
def health_check():
    return {"status": "healthy"}
