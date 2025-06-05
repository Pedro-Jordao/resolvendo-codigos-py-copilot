# Agora vamos solicitar uma string e um número inteiro do usuário, e vamos repetir a string o número de vezes especificado pelo usuário, sem que os dados fiquem concatenados (colados).
def repetir_string():
    # Recebendo a string do usuário
    texto = input("Digite uma string: ")
    
    # Recebendo o número de repetições do usuário
    vezes = int(input("Digite um número inteiro para repetir a string: "))
    
    # Repetindo a string o número de vezes especificado
    resultado = (texto + "\n") * vezes
    # A principal diferença aqui é que estamos adicionando uma quebra de linha após cada repetição da string, evitando que os dados fiquem colados
    # Exibindo o resultado
    print(f"Resultado da repetição:\n{resultado.strip()}")
repetir_string()
# Fim do código