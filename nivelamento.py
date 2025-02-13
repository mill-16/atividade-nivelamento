alt_m = []
alt_f = []

for i in range(15):
    genero = input(f"Pessoa nº {i+1}\nGênero (M - Masculino; F - Feminino): ").lower()

    while genero != "m" and genero != "f":
        print("Resposta inválida. Digite 'M' se o seu gênero for masculino e 'F' se o seu gênero for feminino.")
        genero = input("Gênero (M - Masculino; F - Feminino): ").lower()

    else:
        altura = int(input("Digite a sua altura, em cm, sem casas decimais: "))
        
        while altura <= 0:
            print("Valor inválido. Tente novamente.")
            altura = int(input("Digite a sua altura, em cm, sem casas decimais: "))

        else:
            if genero == "m":
                alt_m.append(altura)
            elif genero == "f":
                alt_f.append(altura)


alt_todos = alt_m + alt_f
print("Maior altura:",max(alt_todos))
print("Menor altura:",min(alt_todos))
 
print("Média de altura das pessoas do gênero masculino:", sum(alt_m)/len(alt_m))
print("Número de pessoas do gênero feminino:", len(alt_f))