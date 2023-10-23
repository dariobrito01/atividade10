# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
km = float(input("digite a veocidade do veiculo em km/h:  "))
vel = 60
multa = (km-60)*7
if vel > int("60"):
    print("sua velocidade esta dentro do padrão estabelecido, por favor pode prossguir com sua viagem. ")
else:
    print(f"sua velocidade excedeu o limite de 60 km/h, você deverá pagar multa de: R${multa} ")



