n=int(input("digite um numero maior que 0 e menor que 1000"))
centenas= n // 100
dezenas= (n // 10)-centenas*10
unidades= (n //1)-dezenas*10-centenas*100
print("as centenas são {} as dezenas {} as unidades {}".format(centenas,dezenas,unidades))


