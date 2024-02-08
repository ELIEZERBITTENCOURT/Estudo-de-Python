from flask import Flask, render_template, request

app = Flask(__name__)

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Não é possível dividir por zero."

@app.route('/')
def index():
    return render_template('calculadora.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
