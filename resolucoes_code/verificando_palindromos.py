# Vamos receber uma palavra do usuário e verificar se ela é um palíndromo!]
def verificar_palindromo():
    # Recebendo a palavra do usuário
    palavra = input("Digite uma palavra: ").strip().lower()
    
    # Verificando se a palavra é um palíndromo
    if palavra == palavra[::-1]:
        print(f"A palavra '{palavra}' é um palíndromo!")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
verificar_palindromo()
# Fim do código