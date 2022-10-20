from efectivo import calculo_efectivo
from sobres import calculo_sobres

def main():
    print('CALCULADORA DE COMPENSACIÓN DE JUECES')
    print('OPCIONES \n 1.Compensación en efectivo \n 2.Compensación en sobres')
    print('--------------------------')
    opcion = int(input('ELEGÍ UNA OPCIÓN: '))
    if opcion == 1:
        calculo_efectivo()
    elif opcion == 2:
        calculo_sobres()

#------------------------------------------------------------------------------
main()
consulta = int(input('¿Querés seguir usando la calculadora? \n 1.SI \n 2.NO \n ELEGÍ UNA OPCIÓN: '))
if consulta == 1:
    main()
    consulta = int(input('¿Querés seguir usando la calculadora? \n 1.SI \n 2.NO \n ELEGÍ UNA OPCIÓN: '))
    while consulta == 1:
        main()
        consulta = int(input('¿Querés seguir usando la calculadora? \n 1.SI \n 2.NO \n ELEGÍ UNA OPCIÓN: '))
if consulta == 2:
    print('¡Gracias, vuelva prontos!')