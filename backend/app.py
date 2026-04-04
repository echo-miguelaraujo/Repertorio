from flask import Flask
from routes.filmes import filmes_bp
from routes.livros import livros_bp
from routes.series import series_bp

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Repertório'

app.register_blueprint(filmes_bp, url_prefix='/filmes')
app.register_blueprint(series_bp, url_prefix='/series')
app.register_blueprint(livros_bp, url_prefix='/livros')

if __name__ == '__main__':
    app.run(debug=True)