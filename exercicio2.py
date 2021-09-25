salario = int(input("Digite o seu salário:"))


reajuste = int(input("Digite o percentual de reajuste do seu salário:"))


novosalario = ((reajuste / 100) * salario) + salario

print("O seu novo salário é: ", novosalario)