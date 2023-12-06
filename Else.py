#Praticas de If/else

#Supondo que se trate de um sistema de limite de velocidade onde o maximo é 110km/h, com If/Else o sistema derteminara uma ordem

velocidade = int(input("Por favor insira sua velocidade"))
if velocidade > 110:
    print("Velocidade acima do limite")
    print("Favor reduzir sua velocidade")
elif velocidade < 60:
    print("Favor aumente sua velocidade")

else:
    print("Velocidade Ok!")




