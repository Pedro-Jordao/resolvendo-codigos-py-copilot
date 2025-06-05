# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles. Tratando possíveis erros na conversão dos dados. 
# O usuário deve poder informar a operação que deseja realizar, e o programa deve validar se a operação é válida.

def operacao_matematica():
    try:
        # Recebendo os números do usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Recebendo a operação desejada
        operacao = input("Digite a operação desejada (+, -, *, /): ")

        # Validando a operação e realizando o cálculo
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ValueError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")

        # Exibindo o resultado
        print(f"Resultado: {resultado}")
    #tratamento de erro caso o usuário não digite um valor numérico
    except ValueError as e:
        print(f"Erro: {e}")
operacao_matematica()
# Fim do código