def calcular_media(sequencia):
    numeros = sequencia.split()  
    numeros_inteiros = [int(num) for num in numeros] 
    soma = sum(numeros_inteiros)  
    media = soma / len(numeros_inteiros)  
    return media

sequencia = input("Digite a sequência de números inteiros separados por espaços: ")
media = calcular_media(sequencia)
print("A média dos números é:", media)
