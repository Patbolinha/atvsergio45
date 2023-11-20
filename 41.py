n1=float(input("digite o primeiro n"))
n2=float(input("digite o segundo n"))
conta=int(input("digite 1 para soma 2 para subtração 3 para multilpicaçao e 4 para divisão"))
if conta==1 and n1+n2>0:
    print("o resultado é: {} e é positivo".format(n1+n2))
elif conta==2:
    print("o resultado é: {}".format(n1-n2))
elif conta==3:
    print("o resultado é: {}".format(n1*n2))
elif conta==4:
    print("o resultado é: {}".format(n1/n2))
