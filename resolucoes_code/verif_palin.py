# Vamos testar se uma palavra é um palíndromo?!
anyWord = input("Digite uma palavra: ");
length = len(anyWord);
newWord = ""
for letter in reversed(anyWord):
    newWord += letter;

if anyWord == newWord:
    print(f"A palavra {anyWord} é um palíndromo")
else:
    print(f"A palavra {anyWord} não é um palíndromo")