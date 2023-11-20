dia = int(input("digite o dia "))
mes = int(input("digite o mes "))
ano = int(input("digite o ano "))

if (dia<32) and (mes<13) and (ano>0):
    print("sua data é valida")
else:
    print("sua data é invalida")