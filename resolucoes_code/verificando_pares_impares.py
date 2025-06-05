# Vamos receber um número inteiro do usuário e verificar se ele é par ou ímpar!
def verificar_par_impar():
    # Recebendo o número inteiro do usuário
    numero = int(input("Digite um número inteiro: "))
    
    # Verificando se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
verificar_par_impar()
# Fim do código