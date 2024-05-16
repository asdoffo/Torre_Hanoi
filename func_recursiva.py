from hanoi_states import ProblemHanoi, StatesHanoi, ActionHanoi
import timeit

def torre_hanoi(n, origen, destino, auxiliar, acciones):
    """
    Si n es igual a 1, simplemente mueve el disco desde la torre de origen a la torre de destino.
    De lo contrario, mueve n-1 discos de la torre de origen a la torre auxiliar utilizando la torre de destino como auxiliar.
    Mueve el disco restante de la torre de origen a la torre de destino.
    Mueve los n-1 discos de la torre auxiliar a la torre de destino utilizando la torre de origen como auxiliar.
    """

    if n == 1:
        #print("Mueva el disco N1 desde la torre", origen, "hasta la torre", destino)
        movimiento = ActionHanoi(disk=n, rod_input=origen, rod_out=destino)
        acciones.append(movimiento)
        return
    torre_hanoi(n - 1, origen, auxiliar, destino, acciones)
    #print("Mueva el disco N", n, "desde la torre", origen, "hasta la torre", destino)
    movimiento = ActionHanoi(disk=n, rod_input=origen, rod_out=destino)
    acciones.append(movimiento)

    torre_hanoi(n - 1, auxiliar, destino, origen, acciones)

    return acciones