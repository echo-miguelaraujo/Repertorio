from flask import Blueprint

filmes_bp = Blueprint('filmes',__name__)

@filmes_bp.route('/')
def filmes():
    return 'Filmes'
