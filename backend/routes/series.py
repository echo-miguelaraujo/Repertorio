from flask import Blueprint

series_bp = Blueprint('series',__name__)

@series_bp.route('/')
def series():
    return 'Series'

