#Programa para calcular batalhas no War
import random
import statistics


def guerra(n_atq, n_def, imprimir):
    '''(int, int, bool) ----> bool
    Função que recebe um número de atacantes e um número de defensores inteiros
    e simula uma batalha de WAR. A variábel boolena imprimir controla se a batalha será impressa
    Retorna True se o atacante vencer, e False caso contrário..'''

    cont = 1 #Contador de batalhas

    # Critérios de parada: 1 atacante restante ou nenhum defensor restante
    #Se uma condição for satisfeita, sai do Loop
    while n_atq > 1 and n_def > 0:

        #Vetores para armazenar os dados de ataque e defesa
        d_atq = []
        d_def = []

        #Verificar cada possibilidade de ataque e defesa

        #Casos com 3 atacantes
        
        if n_atq > 3 and n_def >=3:
            
            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))

        elif n_atq>3 and n_def==2:

            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(0)

        elif n_atq>3 and n_def==1:
            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))

            d_def.append(random.randint(1,6))
            d_def.append(0)
            d_def.append(0)

        #Casos com 2 atacantes

        elif n_atq==3 and n_def >=3:

            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(0)

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))

        elif n_atq==3 and n_def ==2:

            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(0)

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(0)

        elif n_atq==3 and n_def ==1:

            d_atq.append(random.randint(1,6))
            d_atq.append(random.randint(1,6))
            d_atq.append(0)

            d_def.append(random.randint(1,6))
            d_def.append(0)
            d_def.append(0)

        #Casos com 1 atacante

        elif n_atq==2 and n_def>=3:

            d_atq.append(random.randint(1,6))
            d_atq.append(0)
            d_atq.append(0)
            

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))

        elif n_atq==2 and n_def==2:

            d_atq.append(random.randint(1,6))
            d_atq.append(0)
            d_atq.append(0)
            

            d_def.append(random.randint(1,6))
            d_def.append(random.randint(1,6))
            d_def.append(0)

        elif n_atq==2 and n_def==1:

            d_atq.append(random.randint(1,6))
            d_atq.append(0)
            d_atq.append(0)
            

            d_def.append(random.randint(1,6))
            d_def.append(0)
            d_def.append(0)

        #Ordenar vetor com os dados em ordem decrescente
        d_atq = sorted(d_atq, reverse = True) 
        d_def = sorted(d_def, reverse = True)
    
        n_atq_salvo = n_atq
        n_def_salvo = n_def

        n_atq = batalha(d_atq, d_def, n_atq, n_def)[0]
        n_def = batalha(d_atq, d_def, n_atq, n_def)[1]

        if imprimir == True:
            imprimir_batalha(d_atq, d_def,n_atq_salvo, n_def_salvo, n_atq, n_def,cont)

        cont+=1

        if n_atq==1:
            return False;
        if n_def == 0:
            return True;

def probabilidade(n_atq, n_def):
    ''' (int, int) ---> Float
    Função que recebe o número de atacantes e defensores, e retorna a probabilidade de vitória
    dos atacantes. Simulação por Monte Carlo'''

    n_testes = 100 #Quantidade de vezes que uma batalha é simulada para calcular probabilidade
    run = 20 #Quantidade de simulações
    prob=[] #Vetor que armazena a probabilidade ao término de cada n_testes simulações. Ele terá run posições
    for k in range(run):
        vitorias = 0
        for i in range(n_testes):
            if (guerra(n_atq, n_def, imprimir=False)):
                vitorias +=1
        prob.append(vitorias/n_testes * 100)

    prob_final = statistics.mean(prob) #Média das probabilidades
    prob_sd = statistics.stdev(prob) #Desvio padrão das probabilidades

    print("P(vitória) = %.2f +- %.2f %s" %(prob_final, prob_sd,"%"))
    return prob_final, prob_sd;


def batalha(ataque, defesa, n_atq, n_def):
    '''(lista, lista, int, int) ---> (int, int)
    Função que recebe uma lista com os dados de ataque, uma lista com os dados de defesa,
    o número de atacantes, o número de defensores. Calcula as baixas de ataque e defesa
    na batalha e retorna o número de atacantes e defensores após a batalha'''

    for i in range(3):
        if defesa[i]!=0 and ataque[i]!=0:
            if defesa[i]>=ataque[i]:
                n_atq -= 1
            else:
                n_def -= 1

    return n_atq, n_def;

def imprimir_batalha(ataque, defesa,n_atq_antes, n_def_antes, n_atq, n_def, index):
    '''(lista, lista, int, int, int, int, int) ---> void
    Recebe a lista de dados de ataque, de defesa, número de atacantes e defensores antes e depois
    de uma batalha e um índice de batalha. Imprime um relatório com os resultados da batalha'''

    print("\n====== BATALHA ", index, "======")
    print("Atacantes: ", n_atq_antes)
    print("Defensores: ", n_def_antes)
    print("Dados de ataque: ", end="")
    for i in range (3):
        if ataque[i] != 0:
            print(ataque[i], "| ", end="")
    print("\nDados de defesa: ", end="")
    for i in range (3):
        if defesa[i] != 0:
            print(defesa[i], "| ", end="")
    print("\n\nBaixas:")
    print("Baixas de ataque: ", n_atq_antes - n_atq)
    print("Baixas de defesa: ", n_def_antes - n_def)

    if n_atq == 1 or n_def == 0:
        print("\n---------------------------")
        print("RESULTADO FINAL")
        print("Atacantes: ", n_atq)
        print("Defensores: ", n_def)

def main():
    resposta = 's'
    while resposta == 's':
        print("\n------------------------------------------")
        n_atq = int(input("Número de atacantes: "))
        n_def = int(input("Número de defensores: "))

        prob = str(input("\nDeseja calcular a probabilidade de vitória? ('s'/'n'): "))
        if prob == "s":
            probabilidade(n_atq,n_def)

        simular = str(input("\nDeseja simular a batalha? ('s'/'n'): "))
        if simular == "s":
            guerra(n_atq, n_def, imprimir=True)





main()
            
            
    
        
