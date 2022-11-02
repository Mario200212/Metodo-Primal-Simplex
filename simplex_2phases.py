import numpy as np
from math import inf
INFTY = float(inf)

############# Início do algoritmo Simplex ####################
def simplex_method(A,b,c,indexes_b,indexes_n):
    infactivel =  False;running = True; it=0
    while running==True:
        (m,n)=np.shape(A)
        # Passo 1: Solução básica
        # Calculando a solução básica:
        B = A[:,indexes_b]
        N = A[:,indexes_n]
        x_B =np.linalg.solve(B, b) #Resolve o sistema linear B*x_B=b
        x_B=x_B[:,None]
        c_B  = c[indexes_b,None]
        c_N = c[indexes_n,None]

        # Verificando a factiibilidade de x_B
        for i in range(0,m):
            if float(x_B[i][0])<0:
                print("Insira uma solução básica factível")
                infactivel=True
                break

        # Se a solução for infactivel,devemos parar o código
        if infactivel:
            exit()
        #Passo 1.1 : Calculo do valor de f
        f= np.dot(c_B.T,x_B)
        # Passo 2.1: Vetor multiplicador Simplex
        lambd=np.linalg.solve(np.transpose(B),c_B) # Resolve o sistema linear B^T *(lambd)=c_B

        # Passo 2.2: Custos Relativos
        rel_costs= c_N -np.dot(np.transpose(lambd),N).T

        # Passo 2.3: Decidindo qual variável entrará na Base 
            ## OBS.: A variável que deve entrar na base é aquela com o custo mínimo
        
        # Custo Relativo mínimo
        
        min_rel_cost = np.min(rel_costs)

        # Posição do custo relativo mínimo
        
        k=np.argmin(rel_costs) #Variavel x_k sai da base
        
        ##Obs.: a coluna "k" de N deverá ser trocada com uma das colunas da matriz B no final da iteração

        # Passo 3: Teste de Otimalidade
        if min_rel_cost>=0:
            #Chegamos na solução ótima
            break
        #Passo 4: Cálculo da direção simplex (y)
        a_Nk=N[:,[k]]
        y=np.linalg.solve(B,a_Nk)
        

        #Passo 5.1: Determinar se o problema é ilimitado:
        

        if np.max(y)<=0:
            print("O problema é ilimitado")
            exit()

        # Passo 5.2: Determinação da variável a sair da base:
        temp=l=epsilon=0
        min = INFTY
        for i in range(m):
            if y[i][0]>0:
                epsilon=x_B[i][0]/y[i][0]
                temp=epsilon
                if temp<min:
                    min=temp
                    l=i # coluna da matriz B que sai da base
        # Passo 6: Atualização
        B[:,[l]],N[:,[k]]=N[:,[k]],B[:,[l]]
        c_B[[l],:],c_N[[k],:] = c_N[[k],:],c_B[[l],:]
        indexes_b[l] , indexes_n[k] = indexes_n[k],indexes_b[l]
        it+=1
    
    
    return  indexes_b , x_B , c_B , it ,np.dot(c_B.T , x_B)[0][0]


## Passo 1

def simplex_method_phase1(A,b,c):
    m,n = np.shape(A) # m e n representam , respc . , o numero de linhas e colunas de A
    # Resolvendo o problema artificial. Definimos A_art e c_art como a martriz de restrições artificiais e o vetor de custos artificial
    A_art = np.concatenate((A,np.eye(m)),axis=1) # m e n representam , respc . , o numero de linhas e colunas de A
    m_art , n_art = np.shape(A_art) # m_art e n_art representam , respc. , o numero de linhas e colunas de A_art
    c_art = np.concatenate((np.zeros(n_art-m_art),np.ones(m_art))) #Vetor de custos do problema artificial
    indexes_n = [i for i in range(n_art-m_art)] # indices das variaveis nao basicas do prob . artificial
    indexes_b = [j for j in range(n_art-m_art,n_art)] # indices das variaveis basicas do prob . artificial
    #Resolvemos o problema artificial com A_art e c_art como inputs
    indexes_new_b , x_B ,c_B , it, f = simplex_method(A_art,b,c_art,indexes_b,indexes_n)
    indexes_total = [i for i in range(n)] # Representa todos os indices , isto eh , todas as variaveis
    indexes_n = []
    # Encontrando os indices das variaveis nao basicas :
    for i in range(len(indexes_total)):
        if indexes_total[i] not in indexes_new_b:
            indexes_n.append(indexes_total[i])
    print("Resultados fase artificial :")
    simplex_results(it,x_B,indexes_new_b,c_B)
    if(f!=0):
        print("O problema artificial não tem custo ótimo zero. O problema principal não é factível")
        exit() 
    return indexes_new_b , indexes_n # indexes_new_b_b representa o indexes_b da base factivel encontrada

def complete_simplex(A,b,c):
    
    indexes_b,indexes_n = simplex_method_phase1(A,b,c)
    indexes_b , x_B , c_B , it ,_  = simplex_method(A,b,c,indexes_b,indexes_n)
    print("Resultados fase principal:")
    simplex_results(it,x_B,indexes_b,c_B)
    
    
def simplex_results(it,x_B,indexes_b,c_B):
    print("Numero de iteraçoes:" , it+1)
    print("Variaveis básicas ótimas:")
    for i in range(len(indexes_b)):
        print(f"Variavel básica: {indexes_b[i]} Valor: {x_B[i][0]}")
        
    print(f"Valor ótimo da função: {np.dot(c_B.T , x_B)[0][0]} ")

    
########### Defina as matrizes A, b e c do Problema aqui: ###########


#####################################################################
complete_simplex(A,b,c)
