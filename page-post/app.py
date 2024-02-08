from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de posts simulada
posts = [
    {'autor': 'John Doe', 'titulo': 'Primeiro post', 'conteudo': 'Conteúdo do primeiro post.'},
    {'autor': 'Jane Smith', 'titulo': 'Segundo post', 'conteudo': 'Conteúdo do segundo post.'}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/post', methods=['GET', 'POST'])
def novo_post():
    if request.method == 'POST':
        autor = request.form['autor']
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        novo_post = {'autor': autor, 'titulo': titulo, 'conteudo': conteudo}
        posts.append(novo_post)
        return redirect(url_for('index'))
    return render_template('novo_post.html')

if __name__ == '__main__':
    app.run(debug=True)
