from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados fictícios da biblioteca
livros = [
    {'id': 1, 'titulo': 'A Revolta de Atlas', 'autor': 'Ayn Rand', 'emprestado': False},
    {'id': 2, 'titulo': '1984', 'autor': 'George Orwell', 'emprestado': False},
    {'id': 3, 'titulo': 'Dom Quixote', 'autor': 'Miguel de Cervantes', 'emprestado': False}
]

@app.route('/')
def index():
    return render_template('index.html', livros=livros)

@app.route('/emprestar/<int:livro_id>')
def emprestar(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    if livro and not livro['emprestado']:
        livro['emprestado'] = True
    return redirect(url_for('index'))

@app.route('/devolver/<int:livro_id>')
def devolver(livro_id):
    livro = next((livro for livro in livros if livro['id'] == livro_id), None)
    if livro and livro['emprestado']:
        livro['emprestado'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
