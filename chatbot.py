import random

def cumprimento_aleatorio():
    cumprimentos = ['Olá!', 'Oi!', 'E aí!', 'Oi, como posso ajudar?']
    return random.choice(cumprimentos)

def despedida_aleatoria():
    despedidas = ['Até logo!', 'Até mais!', 'Até breve!', 'Tchau!']
    return random.choice(despedidas)

def responder_pergunta(pergunta):
    if 'como você está?' in pergunta.lower():
        return 'Estou bem, obrigado! E você?'
    elif 'qual é o seu nome?' in pergunta.lower():
        return 'Meu nome é Chatbot.'
    elif 'o que você faz?' in pergunta.lower():
        return 'Eu sou um chatbot simples programado para responder a perguntas básicas.'
    else:
        return 'Desculpe, eu não entendi. Pode reformular sua pergunta?'

def main():
    print("Olá! Eu sou um chatbot simples. Digite 'sair' a qualquer momento para encerrar.")

    while True:
        entrada_usuario = input('Você: ')
        
        if entrada_usuario.lower() == 'sair':
            print(despedida_aleatoria())
            break

        if entrada_usuario:
            resposta = responder_pergunta(entrada_usuario)
            print(f'Chatbot: {resposta}')

if __name__ == "__main__":
    main()
