#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.
firstInt = int(input("Digite um valor inteiro: "));
remainder = firstInt % 2;
if remainder == 0:
    print(f"o número {firstInt} é par")
else:
    print(f"o número {firstInt} é impar")

