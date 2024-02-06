from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def process_user_message(user_message):
    if "ola?" in user_message.lower():
        bot_response = "Olá! Como posso ajudar?"
    elif "como você está?" in user_message.lower():
        bot_response = "Eu sou apenas um programa, mas obrigado por perguntar!"
    else:
        bot_response = "Desculpe, não entendi. Pode reformular sua pergunta?"
    return bot_response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    bot_response = process_user_message(user_message)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
