import string

def contar_palavras(texto):
    texto_sem_pontuacao = texto.translate(str.maketrans('', '', string.punctuation))
    numero_palavras = len(texto_sem_pontuacao.split())
    return numero_palavras

texto = input("Digite o texto: ")
numero_palavras = contar_palavras(texto)
print("Número de palavras no texto:", numero_palavras)
