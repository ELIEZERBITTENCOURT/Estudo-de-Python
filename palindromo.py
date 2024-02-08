def eh_palindromo(string):
    string = string.replace(" ", "").lower()
    return string == string[::-1]

entrada = input("Digite uma string para verificar se é um palíndromo: ")

if eh_palindromo(entrada):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
