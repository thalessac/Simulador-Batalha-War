# Programa para calcular batalhas no War
import random
import statistics


def war(n_attackers, n_defenders, print_report=False, attack_thres=None):
    """(int, int, bool) ----> bool
    Função que recebe um número de atacantes e um número de defensores inteiros
    e simula uma batalha de WAR. A variábel boolena imprimir controla se a batalha será impressa
    Retorna True se o atacante vencer, e False caso contrário.."""

    battle_counter = 1

    while n_attackers > 1 and n_defenders > 0:

        attack_dices = [0, 0, 0]
        defense_dices = [0, 0, 0]

        for i in range(min(n_attackers, 3)):
            attack_dices[i] = random.randint(1, 6)
        for i in range(min(n_defenders, 3)):
            defense_dices[i] = random.randint(1, 6)

        attack_dices = sorted(attack_dices, reverse=True)
        defense_dices = sorted(defense_dices, reverse=True)

        initial_n_attackers = n_attackers
        initial_n_defenders = n_defenders

        n_attackers, n_defenders = battle(attack_dices, defense_dices, n_attackers, n_defenders)

        if print_report:
            print_battle_report(
                attack_dices=attack_dices,
                defense_dices=defense_dices,
                initial_n_attackers=initial_n_attackers,
                initial_n_defenders=initial_n_defenders,
                final_n_attackers=n_attackers,
                final_n_defenders=n_defenders,
                index=battle_counter,
            )

        battle_counter += 1

        if n_attackers == 1:
            return False
        if n_defenders == 0:
            return True
        if attack_thres:
            if n_attackers < attack_thres:
                return False


def war_probability(n_attackers, n_defenders):
    """(int, int) ---> Float
    Função que recebe o número de atacantes e defensores, e retorna a probabilidade de vitória
    dos atacantes. Simulação por Monte Carlo"""

    n_testes = 100  # Quantidade de vezes que uma batalha é simulada para calcular probabilidade
    run = 20  # Quantidade de simulações
    prob = []  # Vetor que armazena a probabilidade ao término de cada n_testes simulações. Ele terá run posições
    for _ in range(run):
        vitorias = 0
        for _ in range(n_testes):
            if war(n_attackers, n_defenders):
                vitorias += 1
        prob.append(vitorias / n_testes * 100)

    prob_final = statistics.mean(prob)  # Média das probabilidades
    prob_sd = statistics.stdev(prob)  # Desvio padrão das probabilidades

    print("P(vitória) = %.2f +- %.2f %s" % (prob_final, prob_sd, "%"))
    return prob_final, prob_sd


def battle(attack_dices, defense_dices, n_attackers, n_defenders):
    """(lista, lista, int, int) ---> (int, int)
    Função que recebe uma lista com os dados de ataque, uma lista com os dados de defesa,
    o número de atacantes, o número de defensores. Calcula as baixas de ataque e defesa
    na batalha e retorna o número de atacantes e defensores após a batalha"""

    for i in range(3):
        if defense_dices[i] != 0 and attack_dices[i] != 0:
            if defense_dices[i] >= attack_dices[i]:
                n_attackers -= 1
            else:
                n_defenders -= 1

    return n_attackers, n_defenders


def print_battle_report(
    attack_dices, defense_dices, initial_n_attackers, initial_n_defenders, final_n_attackers, final_n_defenders, index
):
    """(lista, lista, int, int, int, int, int) ---> void
    Recebe a lista de dados de ataque, de defesa, número de atacantes e defensores antes e depois
    de uma batalha e um índice de batalha. Imprime um relatório com os resultados da batalha"""

    print("\n====== BATALHA ", index, "======")
    print("Atacantes: ", initial_n_attackers)
    print("Defensores: ", initial_n_defenders)
    print("Dados de ataque: ", end="")
    for i in range(3):
        if attack_dices[i] != 0:
            print(attack_dices[i], "| ", end="")
    print("\nDados de defesa: ", end="")
    for i in range(3):
        if defense_dices[i] != 0:
            print(defense_dices[i], "| ", end="")
    print("\n\nBaixas:")
    print("Baixas de ataque: ", initial_n_attackers - final_n_attackers)
    print("Baixas de defesa: ", initial_n_defenders - final_n_defenders)

    # if final_n_attackers == 1 or final_n_defenders == 0:
    print("\n---------------------------")
    print("RESULTADO FINAL")
    print("Atacantes: ", final_n_attackers)
    print("Defensores: ", final_n_defenders)
    print("\n")


def main():
    while True:
        print("\n------------------------------------------")
        n_attackers = int(input("Número de atacantes: "))
        n_defenders = int(input("Número de defensores: "))

        prob = str(input("\nDeseja calcular a probabilidade de vitória? ('s'/'n') - 'q' exit: "))
        if prob == "s":
            war_probability(n_attackers, n_defenders)
        elif prob == "q":
            break

        simular = str(input("\nDeseja simular a batalha? ('s'/'n') - 'q' exit: "))
        if simular == "s":
            thres = str(input("\nDeseja informr um limite de atacantes para encerrar a batalha? ('s'/'n'): "))
            if thres == "s":
                thres_value = int(input("-Informe o limite: "))
                war(n_attackers, n_defenders, print_report=True, attack_thres=thres_value)
            else:
                war(n_attackers, n_defenders, print_report=True)
        elif simular == "q":
            break


main()
