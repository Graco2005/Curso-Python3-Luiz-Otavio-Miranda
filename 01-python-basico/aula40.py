'''Calculadora com while'''

print('---Calculadora Python---')

while True:

    num1 = input('Digite o primeiro número para realizar a operação: ')
    num2 = input('Digite o segundo número para realizar a operação: ')
    operacao = input('Escolha que tipo de operação deseja fazer:\n[1]soma\n[2]subtração\n[3]multiplicação\n[4]divisão\n')
    float_num1 = 0
    float_num2 = 0
    int_operacao = 0
    resultado = 0

    try:

        float_num1 = float(num1)
        float_num2 = float(num2)
        int_operacao = int(operacao)

        if int_operacao == 1:
            resultado = float_num1 + float_num2
        elif int_operacao == 2:
            resultado = float_num1 - float_num2
        elif int_operacao == 3:
            resultado = float_num1 * float_num2
        elif int_operacao == 4:
            resultado = float_num1 / float_num2
        else:
            print('Digite um dos números mencionados.')

        print(f'\033[31mResultado\033[0m: {resultado:.2f}')

        sair = input('Deseja [s]air?').lower().startswith('s')
        if sair:
            print('Desligando calculadora...')
            break
    except:
        print('Digite valores válidos.')
