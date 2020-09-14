import numpy as np

lenght = 0.8
nel = 5
rho_e = 1.22           # Considerando ar;
c_e = 340              # Velocidade do som no ar;
A_e = 3.14e-6          # Área da seção transversal, tubo de 2 mm de diâmetro;

def mesh_1D(lenght,nel):
    global coord
    coord = []
    for i in range(nel + 1):
        linha = []
        linha.append(i+1)
        position = np.linspace(0, lenght, nel + 1)
        linha.append(position[i])

        coord.append(linha)
    print(coord)

    global connect
    connect = []
    for j in range(nel):
        linha = []
        linha.append(j+1)
        linha.append(j+1)
        linha.append(j+2)

        connect.append(linha)
    print(connect)

    return coord, connect

mesh_1D(lenght,nel)

element  = [x[0] for x in connect]
node_1 = [x[1] for x in connect]
node_2 = [x[2] for x in connect]
x_el = [x[1] for x in coord]                      # Posição nodal;

aux_K = [[1, -1],
         [-1, 1]]

aux_M = [[2, 1],
         [1, 2]]      

el = 1                                          # Número do elemento em que se deseja as matrizes elementares;

def matrices(el, coord, connect, rho_e, c_e, A_e):
    h_e = []     # Mudar para h_e
    for i in range(nel):
        h_e.append(x_el[i+1] - x_el[i])        # Posição relativa ao nó anterior (comprimento elementar);
    global K_e
    global M_e
    K_e = (A_e/(rho_e * h_e[el])) * np.array(aux_K)
    Ke_0 = rho_e * c_e * c_e                     # Módulo de compressibilidade do elemento;
    M_e = (A_e * h_e[el]/(6*Ke_0))*np.array(aux_M)
    
    return K_e, M_e

matrices(el, coord, connect, rho_e, c_e, A_e) 
print(K_e)
print(M_e)