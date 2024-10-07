#vamos calcular a média de três notas fornecidas na entrada do usuário.

firstGrade = float(input("Digite a primeira nota: "));
secondGrade = float(input("Digite a segunda nota: "));
ThirdGrade = float(input("Digite a terceira nota: "));

average  = (firstGrade + secondGrade + ThirdGrade) / 3;

print(f"e média final do aluno é {average:.2f}")