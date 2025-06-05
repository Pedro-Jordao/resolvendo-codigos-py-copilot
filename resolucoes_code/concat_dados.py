# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!

def concat_dados():
    # Recebendo os dados do usuário
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")

    # Concatenando os dados com espaço entre eles
    resultado = dado1 + " " + dado2

    # Exibindo o resultado
    print(f"Resultado da concatenação: {resultado}")

concat_dados()
# Fim do código