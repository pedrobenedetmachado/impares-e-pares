n = 1
p = 0
i = 0
while n != 0:
    n = int(input('digite um numero (digite 0 para parar): '))
    if n != 0:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1
print(f' você digitou {p} numeros pares e {i} numeros impares ')