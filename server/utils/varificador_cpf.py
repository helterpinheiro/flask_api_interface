def verificando_cpf(cpf):
    # Removendo os caracteres que não sao dígitos
    cpf = ''.join(filter(str.isdigit, cpf))
    print(cpf)
    # Verificando se todos os números são iguais
    if len(set(cpf)) == 1:
        return False

    # Verificando se o CPF possui 11 números
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    digit_1 = 11 - (total % 11)
    if digit_1 > 9:
        digit_1 = 0

    # Calcula o segundo dígito verificador
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    digit_2 = 11 - (total % 11)
    if digit_2 > 9:
        digit_2 = 0

    # Verifica se os dígitos verificadores calculados coincidem com os reais
    if int(cpf[9]) == digit_1 and int(cpf[10]) == digit_2:
        return True
    else:
        return False
  