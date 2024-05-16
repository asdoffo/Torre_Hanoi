from hanoi_states import ProblemHanoi, StatesHanoi, ActionHanoi
from func_recursiva import torre_hanoi
import tracemalloc
import timeit

# Para medir memoria consumida (usamos el pico de memoria)
tracemalloc.start()

# Parámetros
num_discos = 5
varilla_inicio = 0
varilla_aux = 1
varilla_fin = 2

list_acciones=[]

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=num_discos)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=num_discos)
problem = ProblemHanoi(initial=initial_state, goal=goal_state)

print("Lista de acciones: ")
print(torre_hanoi(num_discos, varilla_inicio, varilla_fin, varilla_aux,list_acciones))

last_state=initial_state

for accion in list_acciones:
    last_state = accion.execute(state_hanoi=last_state)
    if last_state == goal_state:  # Comprobamos si hemos alcanzado el estado objetivo
        print("!!!!!!! Encontramos la solución !!!!!!!")


_, memory_peak = tracemalloc.get_traced_memory()
memory_peak /= 1024*1024
tracemalloc.stop()

print("******* Estado inical: "+str(initial_state))
print("******* Estado final: "+str(last_state))
print("******* Costo final: "+str(last_state.accumulated_cost)+" Movimientos")
print(f"******* Máxima memoria ocupada: {round(memory_peak, 3)} [MB]", )
