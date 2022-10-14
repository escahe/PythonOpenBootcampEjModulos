def sumar(*args):
    """
    Recibe como parámetro números a sumar, 
    por ejemplo sumar(1,2,3) retorna 6.
    """
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

def restar(*args):
    """
    Recibe como parámetro números a restar en orden, 
    por ejemplo restar(3,2,1) retorna 0.
    """
    resultado = args[0]
    for i in range(1,len(args)):
        resultado -= args[i]
    return resultado

def multiplicar(*args):
    """
    Recibe como parámetro números a multiplicar, 
    por ejemplo multiplicar(1,2,3) retorna 6.
    """
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado

def dividir(*args):
    """
    Recibe como parámetro números a dividir en orden, 
    por ejemplo dividir(4,2,1) retorna 2.
    """
    try:
        resultado = args[0]
        for i in range(1,len(args)):
            resultado /= args[i]
        return resultado
    except ZeroDivisionError:
        return('No se puede dividir entre cero')