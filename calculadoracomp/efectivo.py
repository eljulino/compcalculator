def calculo_efectivo():
    jueces = int(input('Jueces totales en el torneo: '))
    jug = int(input('Jugadores totales inscriptos: '))
    dinero = int(input('$ por jugador al pozo: '))
    print('¿Hay más eventos en el día? \n 1.SI \n 2.NO')
    confirm = int(input('ELEGÍ UNA OPCIÓN: '))
    comp = dinero * jug
    compTotal = []
    compTotal.append(comp)
    while confirm == 1:
        jug = int(input('Jugadores totales inscriptos: '))
        dinero = int(input('$ por jugador al pozo: '))
        print('¿Hay más eventos en el día? \n 1.SI \n 2.NO')
        confirm = int(input('ELEGÍ UNA OPCIÓN: '))
        comp = dinero * jug
        compTotal.append(comp)
    if jueces > 3:
        hj = int(input('Jueces principales: '))
        tl = int(input('Team Leaders: '))
        floor = int(input('Jueces de piso: '))
        compfloor = int((sum(compTotal) / jueces) * 0.9)
        comptl = int(sum(compTotal) / jueces)
        comphj =  int((sum(compTotal) / jueces) *1.2)
        resto = (sum(compTotal)) - ((compfloor * floor) + (comptl * tl) + (comphj * hj))
        if resto != 0:
            compfloor = int((resto / floor) + compfloor)
        print('El total a repartir es de', sum(compTotal))
        print ('Cada HJ se lleva ', comphj)
        print('Cada TL se lleva ', comptl)
        print('Cada floor se lleva ', compfloor)
    else:
        print('El total a repartir es ', sum(compTotal))
        print('Cada persona se lleva ', sum(compTotal)/jueces)