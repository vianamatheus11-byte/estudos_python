sexo = input("Digite o sexo (M/F): ")

if sexo == "m" or sexo == "M":
    print("Você é do sexo masculino.")
    altura_pai = float(input("Digite a altura do seu pai (em metros): "))
    altura_mae = float(input("Digite a altura da sua mãe (em metros): "))
    altura_filho = (altura_pai + altura_mae) / 2 + 0.13
    print(" A altura do filho será de aproximadamente: ", altura_filho, "metros.")  

if sexo == "f" or sexo == "F": 
    print("Você é do sexo feminino.")
    altura_pai = float(input("Digite a altura do seu pai (em metros): "))
    altura_mae = float(input("Digite a altura da sua mãe (em metros): "))
    altura_filha = (altura_pai + altura_mae) / 2 - 0.13
    print(" A altura da filha será de aproximadamente: ", altura_filha, "metros.")