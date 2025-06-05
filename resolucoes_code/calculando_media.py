# Vamos receber três notas do usuário e calcular a média delas!
def calcular_media():
    # Recebendo as notas do usuário
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calculando a média
    media = (nota1 + nota2 + nota3) / 3

    # Exibindo o resultado
    print(f"A média das notas é: {media:.2f}")
calcular_media()
# Fim do código