from flask import Blueprint

livros_bp = Blueprint('livros',__name__)

@livros_bp.route('/')
def livros():
    return 'Livros'
