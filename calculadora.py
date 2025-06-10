nome_usuario = input('Olá! Por favor, insira seu nome:')
print(f'Ola, {nome_usuario}! Bem vindo à máquina de cálculos')

primeiro_valor = float(input ('digite o primeiro valor: '))
operação_desejada = input ("digite a operação desejada (+, -, *, /, %):")
segundo_valor = float(input('digite o segundo valor: '))

if operação_desejada == '+':
    resultado = primeiro_valor + segundo_valor
elif operação_desejada == '-':
    resultado = primeiro_valor - segundo_valor
elif operação_desejada == '*':
    resultado = primeiro_valor * segundo_valor
elif operação_desejada == '/':
    if segundo_valor != 0:
        resultado = primeiro_valor / segundo_valor
    else:
        resultado = 'Erro: divisão por zero'
elif operação_desejada == '%':
    resultado = (primeiro_valor / 100) * segundo_valor
else:
    resultado = 'Operação inválida'

print(f'Resultado da operação: {resultado}')
