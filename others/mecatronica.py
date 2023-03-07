def rpm_polias(n1, d1, d2):
    rpm_polia = n1 * d1 / d2
    return rpm_polia


def rpm_engrenagens(n1, z1, z2):
    rpm_engrenagen = n1 * z1 / z2
    return rpm_engrenagen


def saidas(rpm):
    saida = rpm * 14 / 61
    return saida


print('''[ 1 ] Para calcular o RPM de polias
[ 2 ] Para calcular o RPM de engrenagens
[ 3 ] Para calcular a saida''')
tipoCalculo = int(input('Digite o numero correspondente a seu objetivo: '))

if tipoCalculo == 1:
    n1User = float(input('Digite o RPM do motor: '))
    d1User = float(input('Digite o diametro da polia motora: '))
    d2User = float(input('Digite o diametro da polia movida: '))
    print(rpm_polias(n1User, d1User, d2User))
if tipoCalculo == 2:
    n1User = float(input('Digite o RPM do motor: '))
    z1User = float(input('Digite o numero de dentes da engrenagem motora: '))
    z2User = float(input('Digite o numero de dentes da engrenagem movida: '))
    print(rpm_engrenagens(n1User, z1User, z2User))
if tipoCalculo == 3:
    rpmUser = float(input('Digite o RPM da movida: '))
    print(saidas(rpmUser))
