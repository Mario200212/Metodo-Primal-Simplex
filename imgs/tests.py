import numpy as np
from simplex_2phases import complete_simplex
#Os problemas devem ser apresentados na forma padrâo , isto é:
#b>0 e todas as restrições na forma de igualdade, com as variaveis de folga já implementadas
 
 #Teste 1  - Funcionando
     
A = np.array([[1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [3, 2, 0, 0, 1]])
c = np.array([-3, -5, 0, 0, 0])
b = np.array([4, 6, 18])

#Teste 2 - Ilimitado

A = np.array([[-1,1,1,0],[-0.5,1,0,1]])
b = np.array([1,2])
c = np.array([-2,-2,0,0])

# Teste 3 - Infactibilidade

b = np.array([24,21,6,3])
c = np.array([-2,-2,0,0,0,0])
A = np.array([[-8,3,1,0,0,0],[3,5,0,-1,0,0],[3,-4,0,0,-1,0],[3,0,0,0,0,1]])


# Teste 4 - Multiplas Soluções

A = np.array([[2,3,4,5,9,19,0,0,0,0,1,0,0],[3,7,17,23,4,1,2,4,5,6,0,1,0],[4,56,2,13,4,5,2,0,0,1,0,0,1]])
b = np.array([15,21,34])
c = np.array([1,10,5,2,3,4,6,7,20,30,0,0,0])


# Teste 5 - Solução Degenerada 

A = np.array([[1,1,1,0,0,0],[1,2,0,1,0,0],[2,1,0,0,1,0],[1,-2,0,0,0,1]])
b = np.array([10,15,15,1])
c = np.array([-3,-5,0,0,0,0])


#Teste 6 - Matrix 3x10

A = np.array([[2,3,4,5,9,19,0,0,0,0],[3,7,17,23,4,1,2,4,5,6],[4,56,2,13,4,5,2,0,0,1]])
b = np.array([15,21,34])
c = np.array([1,10,5,2,3,4,6,7,20,30])
