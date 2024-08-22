def calcular(numero1, numero2, operacion):
    respuesta = 0
    match operacion:
        case '+':
            # Operación suma
            respuesta = numero1 + numero2
        case '-':
            # Operación resta
            respuesta = numero1 - numero2
        case '*':
            # Operación multiplicación
            respuesta = numero1 * numero2
        case '/':
            # Operación division
            respuesta = numero1/numero2
       
        case '^':
            # Operación potencia
            respuesta = numero1**numero2
        case '%':
            # Operación modulo
            respuesta = numero1%numero2

        # TODO: DEBES COLOCAR TU CÓDIGO AQUÍ# TODO: DEBES CREAR AQUÍ LOS CASES PARA LA OPERACIÓN DE LA POTENCIA Y EL MÓDULO, COMPROBANDO LOS SÍMBOLOS ^ Y %.

        case _:
            raise ValueError("Operación inválida.")

    return respuesta

if __name__ == '__main__':
    # Lectura del valor de 2 variables enteras por consola:
    print("Ingrese el número 1")
    numero1 = int(input())
    print("Ingrese el número 2")
    numero2 = int(input())
    # TODO: EN LA SIGUIENTE LÍNEA DEBES ADICIONAR EL SÍMBOLO DE ^ Y % PARA QUE LE APAREZCA AL USUARIO.
    print("Ingrese la operación (+, -, *, /)")
    operacion = input()

    resultado = calcular(numero1, numero2, operacion)
    print("La respuesta es " + str(resultado))
