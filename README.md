# Metodo Simplex - Algoritmo
 ## Implementação do Metodo Simplex em Duas fases
 Nesse projeto, implementamos o Algoritmo Simplex resolvendo o problema artificial para encontrar uma base factível e , a partir desta , resolver o problema primal Simplex.
 ## Fluxo de execução
 ### Inputs 
 Matriz de restrições(A), vetor de custos(c),vetor dos recursos(b)
 ### Outputs 
 Vetor de variaveis basicas ótimas(x_B)[se existir] , valor ótimo da função(f(x_B))

 ## Suposições
 Supomos que os inputs do problema estão na forma padrão, isto é:
 - b >= 0
 - Todos os problemas estão na forma de minimização
 - Todos as restrições estão na forma de igualdade 
    - Isto é: 
        - ![equation](https://latex.codecogs.com/png.image?%5Cbg%7Bwhite%7D%5Ctext%7Bmin%20%7D%20c%5Etx%5Cbegin%7Bcases%7DAx%20%5Cgeq%20b%20%5C%5Cx%5Cgeq%200%5C%5C%5Cend%7Bcases%7D%20%5Cmapsto%20%5Ctext%7B%20min%20%7Dc%5Etx%5Cbegin%7Bcases%7DAx%20&plus;%20Is%20=%20b%5C%5Cx,s%20%5Cgeq%200%5Cend%7Bcases%7D%20)
    - Onde s são as **variaveis de folga** adicionadas 
 ### Primeira Fase
 A primeira fase constitui-se na criação de um problema artificial do tipo:

 ![equation](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D%5Cbg%7Bwhite%7D%5Ctext%7Bmin%20%7D%20%5Csum%5Climits_%7Bi=1%7D%5Em%20%5Clambda_i%20%5Cbegin%7Bcases%7DAx%20&plus;I%5Clambda%20=%20b%20%5C%5Cx,%5Clambda%20%5Cgeq%200%5Cend%7Bcases%7D)
 
 Onde lambda é o vetor das variaveis artificiais criadas para encontrar uma base factivel trivial. Se esse problema tem solução otima com custo zero a partição ótima encontrada corresponde a uma partição factível do problema original. Utilizamos essa partição na seunnda fase, caso ela exista. Caso contrário, o programa é parado.
 
 ### Segunda Fase
 A segunda fase é a resolução do problema primal Simplex da forma usual, cuja demonstração matemática pode ser encontrada nas referências indicadas. Segue o pseudocodigo utilizado

 #### Pseudocódigo
 ![Deletada :( ](imgs/alg1.png)
 ![Deletada :( ](imgs/alg2.png)

 ## Referências
 LUENBERGER , David G.- **Linear and Nonlinear Programming**.4ª Edição.Springer,2016
 
 ARENALES , Marcos - **Pesquisa Operacional**. 1ª Edição.Elsevier,2011

