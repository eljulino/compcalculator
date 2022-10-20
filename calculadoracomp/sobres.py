def calculo_sobres():
    import math
    jueces = int(input('Jueces totales en el torneo: '))
    jug = int(input('Jugadores totales inscriptos: '))
    sobres = float(input('Sobres por jugador al pozo: '))
    print('¿Hay más eventos en el día? \n 1.SI \n 2.NO')
    confirm = int(input('ELEGÍ UNA OPCIÓN: '))
    comp = sobres * jug
    compTotal = []
    compTotal.append(comp)
    while confirm == 1:
        jug = int(input('Jugadores totales inscriptos: '))
        sobres = float(input('Sobres por jugador al pozo: '))
        print('¿Hay más eventos en el día? \n 1.SI \n 2.NO')
        confirm = int(input('ELEGÍ UNA OPCIÓN: '))
        comp = sobres * jug
        compTotal.append(comp)
    if jueces > 3:
        hj = int(input('Jueces principales: '))
        tl = int(input('Team Leaders: '))
        floor = int(input('Jueces de piso: '))
        compfloor = math.floor((sum(compTotal) / jueces) * 0.8)
        comptl = math.floor(sum(compTotal) / jueces)
        comphj =  math.floor((sum(compTotal) / jueces) *1.2)
        resto = math.floor(sum(compTotal)) - ((compfloor * floor) + (comptl * tl) + (comphj * hj))
        if resto != 0:
            compfloor = math.floor((resto / floor) + compfloor)
        print('El total a repartir es de', math.floor(sum(compTotal)), 'sobres')
        print ('Cada HJ se lleva ', comphj, 'sobres')
        print('Cada TL se lleva ', comptl, 'sobres')
        print('Cada floor se lleva ', compfloor, 'sobres')
        print('------------------------------------------')
        print('¿Querés vender tus sobres? \n 1.SI \n 2.NO')
        conversor = int(input('ELEGÍ UNA OPCIÓN: '))
        if conversor == 1:
            valor_sobre = int(input('Valor de compra del sobre: '))
            print('Cada HJ se lleva',valor_sobre*comphj, 'pesos')
            print('Cada TL se lleva', valor_sobre*comptl, 'pesos')
            print('Cada floor se lleva', valor_sobre*compfloor,'pesos')
    else:
        print('El total a repartir es de', math.floor(sum(compTotal)), 'sobres')
        print('Cada persona se lleva', math.floor(sum(compTotal)/jueces), 'sobres')
        print('------------------------------------------')
        print('¿Querés vender tus sobres? \n 1.SI \n 2.NO')
        conversor = int(input('EELEGÍ UNA OPCIÓN: '))
        if conversor == 1:
            valor_sobre = int(input('Valor de compra del sobre: '))
            print('Cada persona se lleva', math.floor(sum(compTotal)/jueces)*valor_sobre, 'pesos')