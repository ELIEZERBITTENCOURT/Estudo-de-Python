def encontrar_ocorrencias(texto, palavra):
    texto_lower = texto.lower()
    palavra_lower = palavra.lower()
    ocorrencias = []
    posicao = texto_lower.find(palavra_lower)
    while posicao != -1:
        ocorrencias.append(posicao)
        posicao = texto_lower.find(palavra_lower, posicao + 1)
    return ocorrencias

texto = input("Digite o texto: ")
palavra = input("Digite a palavra a ser encontrada: ")

posicoes_ocorrencias = encontrar_ocorrencias(texto, palavra)
if posicoes_ocorrencias:
    print("A palavra foi encontrada nas seguintes posições:", posicoes_ocorrencias)
else:
    print("A palavra não foi encontrada no texto.")
