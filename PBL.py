#biblioteca para sortear os numeros da matriz
import random
random.seed()
#funcao para saber a dimensão do tabuleiro e os parametros do sorteio
def dimensao_do_tabuleiro(dificuldade):
    primeiro = 1
    if dificuldade == 1:
        dimensao_da_matriz = 3
        ultimo = 30
    elif dificuldade == 2:
        dimensao_da_matriz = 4
        ultimo = 60
    elif dificuldade == 3:
        dimensao_da_matriz = 5
        ultimo = 100
    return primeiro, ultimo, dimensao_da_matriz
#funcao para gerar o tabuleiro de acordo com a dimensao da matriz e os parametros do sorteio
def gerar_tabuleiro(dificuldade):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    linha = [0] * (dimensao_da_matriz + 1)
    tabuleiro = [linha] * (dimensao_da_matriz + 1)
    lista = []
    for l in range(dimensao_da_matriz):
        linha = []
        for j in range(dimensao_da_matriz):
            elemento = random.randrange(primeiro, ultimo+1)
            while elemento in lista:
                elemento = random.randrange(primeiro, ultimo+1)
            if elemento not in lista:
                linha.append(elemento)
                lista.append(elemento)
        linha.append(0)
        tabuleiro[l] = linha
    return tabuleiro
#funcao para gerar a quantidade de tabuleiros necessarios
def quantidade_de_tabuleiros(modo_de_jogo,dificuldade):
    if modo_de_jogo == 1:
        tabuleiro_dos_jogadores = gerar_tabuleiro(dificuldade)
        return tabuleiro_dos_jogadores, 0
    elif modo_de_jogo == 2:
        tabuleiro_do_jogador1 = gerar_tabuleiro(dificuldade)
        tabuleiro_do_jogador2 = gerar_tabuleiro(dificuldade)
        return tabuleiro_do_jogador1, tabuleiro_do_jogador2
#funcao para gerar tabuleiro vazio
def gerar_tabuleiro_vazio(dificuldade):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    tabuleiro_vazio = []
    for l in range(dimensao_da_matriz +1):
        linha = []
        for j in range(dimensao_da_matriz +1):
            linha.append("X")
        tabuleiro_vazio.append(linha)
    return tabuleiro_vazio
#funcao para gerar a quantidade de tabuleiros vazios necessarios
def quantidade_de_tabuleiros_vazio(modo_de_jogo, dificuldade):
    if modo_de_jogo == 1:
        tabuleiro_vazio_dos_jogadores = gerar_tabuleiro_vazio(dificuldade)
        return tabuleiro_vazio_dos_jogadores, 0
    elif modo_de_jogo == 2:
        tabuleiro_vazio_do_jogador1 = gerar_tabuleiro_vazio(dificuldade)
        tabuleiro_vazio_do_jogador2 = gerar_tabuleiro_vazio(dificuldade)
        return tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2
#funcao para somar e atribuir a soma a ultima linha e a ultima coluna de cada indice
def soma_linha_coluna(dificuldade,tabuleiro_do_jogador1, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for l in range(dimensao_da_matriz):
        soma_linha_ta1 = soma_linha_ta2 = soma_coluna_ta1 = soma_coluna_ta2 =0
        for j in range(dimensao_da_matriz+1):
            if j != dimensao_da_matriz:
                soma_linha_ta1 += tabuleiro_do_jogador1[l][j]
                soma_coluna_ta1 += tabuleiro_do_jogador1[j][l]
                if tabuleiro_do_jogador2 != 0:
                    soma_linha_ta2 += tabuleiro_do_jogador2[l][j]
                    soma_coluna_ta2 += tabuleiro_do_jogador2[j][l]
            elif j == dimensao_da_matriz:
                tabuleiro_do_jogador1[l][j] = soma_linha_ta1
                tabuleiro_do_jogador1[j][l] = soma_coluna_ta1
                if tabuleiro_do_jogador2 != 0:
                    tabuleiro_do_jogador2[l][j] = soma_linha_ta2
                    tabuleiro_do_jogador2[j][l] = soma_coluna_ta2
    return tabuleiro_do_jogador1, tabuleiro_do_jogador2
#funcao para revelar o menor valor da linha de um indice do tabuleiro1
def revelar_menor_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    menor = 500
    for j in range(dimensao_da_matriz):
        if tabuleiro_do_jogador1[linha_coluna_tabuleiro][j] < menor and tabuleiro_do_jogador1[linha_coluna_tabuleiro][j] != tabuleiro_vazio_do_jogador1[linha_coluna_tabuleiro][j]:
            menor = tabuleiro_do_jogador1[linha_coluna_tabuleiro][j]
            coluna_indice = j
    tabuleiro_vazio_do_jogador1[linha_coluna_tabuleiro][coluna_indice] = menor
    return tabuleiro_vazio_do_jogador1
#funcao para revelar o maior valor da linha de um indice do tabuleiro1
def revelar_maior_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    maior = 0
    for j in range(dimensao_da_matriz):
        if tabuleiro_do_jogador1[linha_coluna_tabuleiro][j] > maior and tabuleiro_do_jogador1[linha_coluna_tabuleiro][j] != tabuleiro_vazio_do_jogador1[linha_coluna_tabuleiro][j]:
            maior = tabuleiro_do_jogador1[linha_coluna_tabuleiro][j]
            coluna_indice = j
    tabuleiro_vazio_do_jogador1[linha_coluna_tabuleiro][coluna_indice] = maior
    return tabuleiro_vazio_do_jogador1
#funcao para revelar toda a linha de um indice
def revelar_toda_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for j in range(dimensao_da_matriz+1):
        if tabuleiro_do_jogador1[linha_coluna_tabuleiro][j] not in tabuleiro_vazio_do_jogador1:
            tabuleiro_vazio_do_jogador1[linha_coluna_tabuleiro][j] = tabuleiro_do_jogador1[linha_coluna_tabuleiro][j]
    return tabuleiro_vazio_do_jogador1
#funcao para revelar o menor valor da coluna de um indice do tabuleiro1
def revelar_menor_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    menor = 500
    for l in range(dimensao_da_matriz):
        if tabuleiro_do_jogador1[l][linha_coluna_tabuleiro] < menor and tabuleiro_do_jogador1[l][linha_coluna_tabuleiro] != tabuleiro_vazio_do_jogador1[l][linha_coluna_tabuleiro]:
            menor = tabuleiro_do_jogador1[l][linha_coluna_tabuleiro]
            linha_indice = l
    tabuleiro_vazio_do_jogador1[linha_indice][linha_coluna_tabuleiro] = menor
    return tabuleiro_vazio_do_jogador1
#funcao para revelar o maior valor da coluna de um indice do tabuleiro1
def revelar_maior_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    maior = 0
    for l in range(dimensao_da_matriz):
        if tabuleiro_do_jogador1[l][linha_coluna_tabuleiro] > maior and tabuleiro_do_jogador1[l][linha_coluna_tabuleiro] != tabuleiro_vazio_do_jogador1[l][linha_coluna_tabuleiro]:
            maior = tabuleiro_do_jogador1[l][linha_coluna_tabuleiro]
            linha_indice = l
    tabuleiro_vazio_do_jogador1[linha_indice][linha_coluna_tabuleiro] = maior
    return tabuleiro_vazio_do_jogador1
#funcao para revelar toda coluna de um indice do tabuleiro1
def revelar_toda_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for l in range(dimensao_da_matriz+1):
        if tabuleiro_do_jogador1[l][linha_coluna_tabuleiro] not in tabuleiro_vazio_do_jogador1:
            tabuleiro_vazio_do_jogador1[l][linha_coluna_tabuleiro] = tabuleiro_do_jogador1[l][linha_coluna_tabuleiro]
    return tabuleiro_vazio_do_jogador1
#funcao para revelar o menor valor da linha de um indice do tabuleiro2
def revelar_menor_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    menor = 500
    for j in range(dimensao_da_matriz):
        if tabuleiro_do_jogador2[linha_coluna_tabuleiro][j] < menor and tabuleiro_do_jogador2[linha_coluna_tabuleiro][j] != tabuleiro_vazio_do_jogador2[linha_coluna_tabuleiro][j]:
            menor = tabuleiro_do_jogador2[linha_coluna_tabuleiro][j]
            coluna_indice = j
    tabuleiro_vazio_do_jogador2[linha_coluna_tabuleiro][coluna_indice] = menor
    return tabuleiro_vazio_do_jogador2
#funcao para revelar o maior valor da linha de um indice do tabuleiro2
def revelar_maior_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    maior = 0
    for j in range(dimensao_da_matriz):
        if tabuleiro_do_jogador2[linha_coluna_tabuleiro][j] > maior and tabuleiro_do_jogador2[linha_coluna_tabuleiro][j] != tabuleiro_vazio_do_jogador2[linha_coluna_tabuleiro][j]:
            maior = tabuleiro_do_jogador2[linha_coluna_tabuleiro][j]
            coluna_indice = j
    tabuleiro_vazio_do_jogador2[linha_coluna_tabuleiro][coluna_indice] = maior
    return tabuleiro_vazio_do_jogador2
#funcao para revelar toda linha de um indice do tabuleiro2
def revelar_toda_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for j in range(dimensao_da_matriz+1):
        if tabuleiro_do_jogador2[linha_coluna_tabuleiro][j] not in tabuleiro_vazio_do_jogador2:
            tabuleiro_vazio_do_jogador2[linha_coluna_tabuleiro][j] = tabuleiro_do_jogador2[linha_coluna_tabuleiro][j]
    return tabuleiro_vazio_do_jogador2
#funcao para revelar o menor valor da coluna de um indice do tabuleiro2
def revelar_menor_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    menor = 500
    for l in range(dimensao_da_matriz):
        if tabuleiro_do_jogador2[l][linha_coluna_tabuleiro] < menor and tabuleiro_do_jogador2[l][linha_coluna_tabuleiro] != tabuleiro_vazio_do_jogador2[l][linha_coluna_tabuleiro]:
            menor = tabuleiro_do_jogador2[l][linha_coluna_tabuleiro]
            linha_indice = l
    tabuleiro_vazio_do_jogador2[linha_indice][linha_coluna_tabuleiro] = menor
    return tabuleiro_vazio_do_jogador2
#funcao para revelar o maior valor da coluna de um indice do tabuleiro2
def revelar_maior_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    maior = 0
    for l in range(dimensao_da_matriz):
        if tabuleiro_do_jogador2[l][linha_coluna_tabuleiro] > maior and tabuleiro_do_jogador2[l][linha_coluna_tabuleiro] != tabuleiro_vazio_do_jogador2[l][linha_coluna_tabuleiro]:
            maior = tabuleiro_do_jogador2[l][linha_coluna_tabuleiro]
            linha_indice = l
    tabuleiro_vazio_do_jogador2[linha_indice][linha_coluna_tabuleiro] = maior
    return tabuleiro_vazio_do_jogador2
#funcao para revelar toda coluna de um indice do tabuleiro2
def revelar_toda_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for l in range(dimensao_da_matriz+1):
        if tabuleiro_do_jogador2[l][linha_coluna_tabuleiro] not in tabuleiro_vazio_do_jogador2:
            tabuleiro_vazio_do_jogador2[l][linha_coluna_tabuleiro] = tabuleiro_do_jogador2[l][linha_coluna_tabuleiro]
    return tabuleiro_vazio_do_jogador2
#funcao para indentificar se todas as casas de uma linha ou coluna do tabuleiro1 foram reveladas
def revelar_soma_linha_coluna_jogador1(dificuldade,tabuleiro_vazio_do_jogador1, tabuleiro_do_jogador1):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for l in range(dimensao_da_matriz):
        casas_reveladas = 0
        casas_reveladas1 = 0
        for j in range(dimensao_da_matriz):
            if tabuleiro_vazio_do_jogador1[l][j] != "X":
                casas_reveladas +=1
            if tabuleiro_vazio_do_jogador1[j][l] != "X":
                casas_reveladas1 +=1
        if casas_reveladas == dimensao_da_matriz:
            tabuleiro_vazio_do_jogador1[l][dimensao_da_matriz] = tabuleiro_do_jogador1[l][dimensao_da_matriz]
        if casas_reveladas1 == dimensao_da_matriz:
            tabuleiro_vazio_do_jogador1[dimensao_da_matriz][l] = tabuleiro_do_jogador1[dimensao_da_matriz][l]
    return tabuleiro_vazio_do_jogador1
#funcao para indentificar se todas as casas de uma linha ou coluna do tabuleiro2 foram reveladas
def revelar_soma_linha_coluna_jogador2(dificuldade,tabuleiro_vazio_do_jogador2, tabuleiro_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    for l in range(dimensao_da_matriz):
        casas_reveladas = 0
        casas_reveladas1 = 0
        for j in range(dimensao_da_matriz):
            if tabuleiro_vazio_do_jogador2[l][j] != "X":
                casas_reveladas +=1
            if tabuleiro_vazio_do_jogador2[j][l] != "X":
                casas_reveladas1 +=1
        if casas_reveladas == dimensao_da_matriz:
            tabuleiro_vazio_do_jogador2[l][dimensao_da_matriz] = tabuleiro_do_jogador2[l][dimensao_da_matriz]
        if casas_reveladas1 == dimensao_da_matriz:
            tabuleiro_vazio_do_jogador2[dimensao_da_matriz][l] = tabuleiro_do_jogador2[dimensao_da_matriz][l]
    return tabuleiro_vazio_do_jogador2
#funcao que chamar outras funcoes para revelar casas no tabuleiro1
def revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo):
    if linha_coluna[indice_jo] == "L":
        if somas[indice_jo] < tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador1 = revelar_menor_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
        elif somas[indice_jo] > tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador1 = revelar_maior_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1,linha_coluna_tabuleiro, tabuleiro_do_jogador1)
        elif somas[indice_jo] == tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador1 = revelar_toda_linha_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
    elif linha_coluna[indice_jo] == "C":
        if somas[indice_jo] < tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador1 = revelar_menor_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
        elif somas[indice_jo] > tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador1 = revelar_maior_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
        elif somas[indice_jo] == tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador1 = revelar_toda_coluna_tabuleiro1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
    tabuleiro_vazio_do_jogador1 = revelar_soma_linha_coluna_jogador1(dificuldade, tabuleiro_vazio_do_jogador1, tabuleiro_do_jogador1)
    return tabuleiro_vazio_do_jogador1
#funcao que chamar outras funcoes para revelar casas no tabuleiro2
def revelar_tab2(dificuldade, tabuleiro_vazio_do_jogador2, tabuleiro_do_jogador2, linha_coluna, somas, linha_coluna_tabuleiro, dimensao_da_matriz, indice_jo):
    if linha_coluna[indice_jo] == "L":
        if somas[indice_jo] < tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador2 = revelar_menor_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
        elif somas[indice_jo] > tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador2 = revelar_maior_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2,linha_coluna_tabuleiro, tabuleiro_do_jogador2)
        elif somas[indice_jo] == tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]:
            tabuleiro_vazio_do_jogador2 = revelar_toda_linha_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
    elif linha_coluna[indice_jo] == "C":
        if somas[indice_jo] < tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador2 = revelar_menor_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
        elif somas[indice_jo] > tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador2 = revelar_maior_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
        elif somas[indice_jo] == tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]:
            tabuleiro_vazio_do_jogador2 = revelar_toda_coluna_tabuleiro2(dificuldade, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
    tabuleiro_vazio_do_jogador2 = revelar_soma_linha_coluna_jogador2(dificuldade,tabuleiro_vazio_do_jogador2, tabuleiro_do_jogador2)
    return tabuleiro_vazio_do_jogador2
#funcao que conta a quantidade de casas nao reveladas antes de revelar as casas
def indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    vazios_inicial = 0
    for l in range(dimensao_da_matriz):
        for j in range(dimensao_da_matriz):
            if tabuleiro_vazio_do_jogador2 == 0:
                if indice_jo == 0 or indice_jo == 1:
                    if tabuleiro_vazio_do_jogador1[l][j] == "X":
                        vazios_inicial +=1
            elif tabuleiro_vazio_do_jogador2 != 0:
                if indice_jo == 0:
                    if tabuleiro_vazio_do_jogador1[l][j] == "X":
                        vazios_inicial +=1
                elif indice_jo == 1:
                    if tabuleiro_vazio_do_jogador2[l][j] == "X":
                        vazios_inicial +=1
    return vazios_inicial
#funcao que conta a quantidade de casas nao reveladas apos revelar as casas
def indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    vazios_final = 0
    for l in range(dimensao_da_matriz):
        for j in range(dimensao_da_matriz):
            if tabuleiro_vazio_do_jogador2 == 0:
                if indice_jo == 0 or indice_jo == 1:
                    if tabuleiro_vazio_do_jogador1[l][j] == "X":
                        vazios_final +=1
            elif tabuleiro_vazio_do_jogador2 !=0:
                if indice_jo == 0:
                    if tabuleiro_vazio_do_jogador1[l][j] == "X":
                        vazios_final +=1
                elif indice_jo == 1:
                    if tabuleiro_vazio_do_jogador2[l][j] == "X":
                        vazios_final +=1
    revelados = vazios_inicial - vazios_final
    if revelados < 0:
        revelados *= -1
    if indice_jo == 0:
        pontos_jogador1 +=revelados
    elif indice_jo == 1:
        pontos_jogador2 +=revelados
    return pontos_jogador1, pontos_jogador2
#funcao para mostrar os tabuleiros necessarios em forma de matriz e enfeites
def mostrar_tabuleiro(tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, dificuldade, jogador1, jogador2):
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)
    if tabuleiro_vazio_do_jogador2 == 0:
        print("Tabuleiro do {} e do {}".format(jogador1, jogador2))
        print("-"*(19+len(jogador1)+len(jogador2)))
        for l in range(dimensao_da_matriz+1):
            print("[", end="")
            for j in range(dimensao_da_matriz+1):
                if j == dimensao_da_matriz:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador1[l][j]), end="")
                else:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador1[l][j]), end="")
            print("]", end="")
            print()
        print("-"*(19+(len(jogador1)+len(jogador2))))
    else:
        if dimensao_da_matriz == 3:
            print("-"*59)
        elif dimensao_da_matriz == 4:
            print("-"*69)
        else:
            print("-"*79)
        print("Tabuleiro do {}".format(jogador1), end="")
        if dimensao_da_matriz == 3:
            espaco = (15+len(jogador1))-24
            if espaco < 0:
                espaco*= -1
            espaco +=15
        elif dimensao_da_matriz == 4:
            espaco = (15+len(jogador1))-29
            if espaco < 0:
                espaco *=-1
            espaco +=15
        else:
            espaco = (15+len(jogador1))-34
            if espaco < 0:
                espaco *=-1
            espaco +=15
        print(" "*espaco,end="")
        print("Tabuleiro do {}".format(jogador2))
        if dimensao_da_matriz == 3:
            print("-"*59)
        elif dimensao_da_matriz == 4:
            print("-"*69)
        else:
            print("-"*79)
        for l in range(dimensao_da_matriz+1):
            print("[", end="")
            for j in range(dimensao_da_matriz+1):
                if j == dimensao_da_matriz:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador1[l][j]), end="")
                else:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador1[l][j]), end="")
            print("]", end="")
            print('               ',end='')
            print("[",end="")
            for k in range(dimensao_da_matriz+1):
                if k == dimensao_da_matriz:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador2[l][k]), end="")
                else:
                    print("{:^5}".format(tabuleiro_vazio_do_jogador2[l][k]), end="")
            print("]",end="")
            print()
        if dimensao_da_matriz == 3:
            print("-"*59)
        elif dimensao_da_matriz == 4:
            print("-"*69)
        else:
            print("-"*79)
#funcao para guardar o historico de jogadas do jogador1 ou dos dois jogadores
def historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1):
    if jogada[0] == "C":
        if soma < tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]:
            historico_jogador1.append(f"{soma}<{jogada}")
        elif soma > tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]:
                historico_jogador1.append(f"{soma}>{jogada}")
        else:
            historico_jogador1.append(f"{soma}={jogada}")
    else:
        if soma < tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]:
            historico_jogador1.append(f"{soma}<{jogada}")
        elif soma > tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]:
            historico_jogador1.append(f"{soma}>{jogada}")
        else:
            historico_jogador1.append(f"{soma}={jogada}")
    return historico_jogador1
#funcao para guardar o historico de jogadas do jogador2
def historico_jo2(soma, historico_jogador2, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador2):
    if jogada[0] == "C":
        if soma < tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]:
            historico_jogador2.append(f"{soma}<{jogada}")
        elif soma > tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]:
                historico_jogador2.append(f"{soma}>{jogada}")
        else:
            historico_jogador2.append(f"{soma}={jogada}")
    else:
        if soma < tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]:
            historico_jogador2.append(f"{soma}<{jogada}")
        elif soma > tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]:
            historico_jogador2.append(f"{soma}>{jogada}")
        else:
            historico_jogador2.append(f"{soma}={jogada}")
    return historico_jogador2
#funcao para verificar se uma linha ou coluna inteira ja foi revelada
def validacao_linha_coluna_tabuleiro(dimensao_da_matriz, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, vez_do_jogador):
    pode = 0
    if tabuleiro_vazio_do_jogador2 == 0 or tabuleiro_vazio_do_jogador2 != 0 and vez_do_jogador == 1:
        if linha_coluna_tabuleiro[0] == "L":
            linha_indice = int(linha_coluna_tabuleiro[1])
            for j in range(dimensao_da_matriz):
                if tabuleiro_vazio_do_jogador1[linha_indice][j] == "X":
                    pode +=1
        else:
            coluna_indice = int(linha_coluna_tabuleiro[1])
            for l in range(dimensao_da_matriz):
                if tabuleiro_vazio_do_jogador1[l][coluna_indice] == "X":
                    pode +=1
    else:
        if linha_coluna_tabuleiro[0] == "L":
            linha_indice = int(linha_coluna_tabuleiro[1])
            for j in range(dimensao_da_matriz):
                if tabuleiro_vazio_do_jogador2[linha_indice][j] == "X":
                    pode +=1
        else:
            coluna_indice = int(linha_coluna_tabuleiro[1])
            for l in range(dimensao_da_matriz):
                if tabuleiro_vazio_do_jogador2[l][coluna_indice] == "X":
                    if tabuleiro_vazio_do_jogador2[l][coluna_indice] == "X":
                        pode +=1
    return pode
#funcao para a jogabilidade
def main():
    print("------NOME DOS JOGADORES------")
    #funcao para perguntar ao usuario os nomes dos jogadores
    jogadores = input("Qual o nome dos jogadores\n:").split(" ")
    #validacao
    while jogadores[0].isalpha()==False or jogadores[1].isalpha()==False:
        print("Digite nomes válidos!")
        jogadores = input("Qual o nome dos jogadores\n:").split(" ")
    print()

    #funcao para sortear quem vai ser o jogador1 e quem vai ser o jogador2
    sortear = random.randrange(1, 3)
    if sortear == 1:
        jogador1 = jogadores[0].upper()
        jogador2 = jogadores[1].upper()
    else:
        jogador2 = jogadores[0].upper()
        jogador1 = jogadores[1].upper()
    print("{} é o jogador 1 e {} é o jogador 2!".format(jogador1, jogador2))
    print("------------------------------")
    print("---QUANTIDADE DE TABULEIROS---")
    #funcao para perguntar ao usuario a quantidade de tabuleiros
    modo_de_jogo = input("1. Um Tabuleiro\n2. Dois Tabuleiros\n:")
    #validacao
    while modo_de_jogo.isdigit()==False or int(modo_de_jogo) > 2 or int(modo_de_jogo) < 1:
        print("Digite um número válido!")
        modo_de_jogo = input("1. Um Tabuleiro\n2. Dois Tabuleiros\n:")
    modo_de_jogo = int(modo_de_jogo)
    print("------------------------------")

    print("---------MODO DE JOGO---------")
    #funcao para perguntar ao usuario a dificuldade do jogo
    dificuldade = input("1. Fácil\n2. Médio\n3. Difícil\n:")
    #validacao
    while dificuldade.isdigit()==False or int(dificuldade) > 3 or int(dificuldade) < 1:
        print("Digite um número válido!")
        dificuldade= input("1. Fácil\n2. Médio\n3. Difícil\n:")
    dificuldade = int(dificuldade)
    print("------------------------------")
    
    #funcao chamada para pegar o tabuleiro_do_jogador1 e o tabuleiro_do_jogador2
    tabuleiro_do_jogador1, tabuleiro_do_jogador2 = quantidade_de_tabuleiros(modo_de_jogo,dificuldade)
    
    #funcao chamada para pegar o tabuleiro_vazio_do_jogador1 e o tabuleiro_vazio_do_jogador2
    tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2 = quantidade_de_tabuleiros_vazio(modo_de_jogo,dificuldade)

    print("---------ENCERRAR JOGO--------")
    #funcao para perguntar ao usuario como ele quer encerrar o jogo
    fim_de_jogo = input("1. Número de Rodadas\n          ou\n2. Tabuleiro Completo\n:")
    #validacao
    while fim_de_jogo.isdigit()==False or int(fim_de_jogo) > 2 or int(fim_de_jogo) < 1:
        print("Digite um número válido!")
        fim_de_jogo = input("1. Número de Rodadas\n          ou\n2. Tabuleiro Completo\n:")
    fim_de_jogo = int(fim_de_jogo)

    if fim_de_jogo == 1:
        #funcao para perguntar ao usuario quantas rodadas ele quer
        rodadas = input("Quantas rodadas\n:")
        #validacao
        while rodadas.isdigit()==False or int(rodadas) % 2 == 0:
            print("O número de rodadas têm que ser positivo e têm que ser ímpar!")
            rodadas = input("Quantas rodadas\n:")
        rodadas = int(rodadas)
    else:
        rodadas = 1000000
    print("------------------------------")

    #funcao para chamar tabuleiro_do_jogador1 e o tabuleiro_do_jogador2 com a soma das linha e colunas
    tabuleiro_do_jogador1, tabuleiro_do_jogador2 = soma_linha_coluna(dificuldade,tabuleiro_do_jogador1, tabuleiro_do_jogador2)
    
    #funcao para chamar primeiro, ultimo e dimensao_da_matriz
    primeiro, ultimo, dimensao_da_matriz = dimensao_do_tabuleiro(dificuldade)

    #declarando variaveis para contar os pontos e listas para guardar o historico
    pontos_jogador1 = pontos_jogador2 = 0
    historico_jogador1 = []
    historico_jogador2 = []
    #condicional por condicao para continuar enquanto o numero de rodadas for maior que 0
    while rodadas > 0:

        #declrando variavel para contar a vez do jogador
        vez_do_jogador = 0

        #declarando listas para guardar a soma dos dois jogadores e a linha ou coluna que o usuario escolheu
        somas = []
        linha_coluna = []
        linha_coluna_indice = []

        #condicional para indentificar caso o tabuleiro do jogador 1 ou o tabuleiro do jogador 2 estiver todo completo
        if tabuleiro_vazio_do_jogador2 == 0 and (pontos_jogador1+pontos_jogador2) == (dimensao_da_matriz*dimensao_da_matriz) or tabuleiro_vazio_do_jogador2 != 0 and pontos_jogador1 == (dimensao_da_matriz*dimensao_da_matriz) or tabuleiro_vazio_do_jogador2 != 0 and pontos_jogador2 == (dimensao_da_matriz*dimensao_da_matriz):
            rodadas = 0
        print("--------------------------------Placar-------------------------------")

        #funcao para mostrar os pontos do jogador1 e os pontos do jogador2
        print("    {}:{} pontos.                         {}:{} pontos.".format(jogador1, pontos_jogador1, jogador2, pontos_jogador2))
        print("---------------------------------------------------------------------")

        #funcao para mostrar ao usuario os tabuleiros necessarios
        mostrar_tabuleiro(tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, dificuldade, jogador1, jogador2)
        
        #condicional para indentificar se o numero de rodadas e maior que 0
        if rodadas > 0:

            #repeticao por contagem para perguntar duas vezes a linha_coluna_tabuleiro e a soma
            for i in range(2):
                vez_do_jogador +=1
                if vez_do_jogador == 1:
                    print("Vez do {}".format(jogador1))
                else:
                    print("Vez do {}".format(jogador2))
                #funcao para perguntar ao usuario a linha ou coluna que ele quer
                linha_coluna_tabuleiro = input("Digite uma linha ou coluna que vá de 0 à {}\n:".format(dimensao_da_matriz-1)).upper()
                #validacao
                if dimensao_da_matriz == 3:
                    dimensao = ["C0", "C1", "C2", "L0", "L1", "L2"]
                elif dimensao_da_matriz == 4:
                    dimensao = ["C0", "C1", "C2", "C3", "L0", "L1", "L2", "L3"]
                else:
                    dimensao = ["C0", "C1", "C2", "C3", "C4", "L0", "L1", "L2", "L3", "L4"]
                while linha_coluna_tabuleiro not in dimensao or validacao_linha_coluna_tabuleiro(dimensao_da_matriz, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, linha_coluna_tabuleiro, vez_do_jogador) == 0:
                    print("Digite uma linha ou coluna válida!")
                    linha_coluna_tabuleiro = input("Digite uma linha ou coluna que vá de 0 à {}\n:".format(dimensao_da_matriz-1)).upper()

                #funcao para perguntar ao usuario a soma da linha ou coluna
                soma = input("Qual a soma\n:")
                #validacao
                while soma.isdigit()==False:
                    print("Digite um número válido!")
                    soma = input("Qual a soma\n:")
                soma = int(soma)
                somas.append(soma)
                linha_coluna.append(linha_coluna_tabuleiro[0])
                
                #condicional para indentificar se eu vou trabalhar com o tabuleiro1
                if tabuleiro_do_jogador2 == 0:
                    #condicional para indenticicar se eu vou manipular uma coluna
                    if linha_coluna_tabuleiro[0] == "C":
                        jogada = linha_coluna_tabuleiro
                        linha_coluna_tabuleiro = linha_coluna_tabuleiro.replace("C","")
                        linha_coluna_tabuleiro= int(linha_coluna_tabuleiro)
                        linha_coluna_indice.append(linha_coluna_tabuleiro)
                        if vez_do_jogador == 1:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca = soma - tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]
                            if diferenca < 0:
                                diferenca *= -1
                        if vez_do_jogador == 2:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca1 = soma - tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]
                            if diferenca1 < 0:
                                diferenca1 *= -1
                    #condicional para indenticicar se eu vou manipular uma linha
                    else:
                        jogada = linha_coluna_tabuleiro
                        linha_coluna_tabuleiro = linha_coluna_tabuleiro.replace("L","")
                        linha_coluna_tabuleiro = int(linha_coluna_tabuleiro)
                        linha_coluna_indice.append(linha_coluna_tabuleiro)
                        if vez_do_jogador == 1:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca = soma - tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]
                            if diferenca < 0:
                                diferenca *= -1
                        if vez_do_jogador == 2:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca1 = soma - tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]
                            if diferenca1 < 0:
                                diferenca1 *= -1

                #condicional para indentificar se eu vou trabalhar com o tabuleiro1 e tabuleiro2
                else:
                    #condicional para indenticicar se eu vou manipular uma coluna
                    if linha_coluna_tabuleiro[0] == "C":
                        jogada = linha_coluna_tabuleiro
                        linha_coluna_tabuleiro = linha_coluna_tabuleiro.replace("C","")
                        linha_coluna_tabuleiro= int(linha_coluna_tabuleiro)
                        linha_coluna_indice.append(linha_coluna_tabuleiro)
                        #condicional para saber a vez do jogador 1
                        if vez_do_jogador == 1:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca = soma - tabuleiro_do_jogador1[dimensao_da_matriz][linha_coluna_tabuleiro]
                            if diferenca < 0:
                                diferenca *= -1
                        #condicional para saber a vez do jogador 2
                        if vez_do_jogador == 2:
                            historico_jogador2 = historico_jo2(soma, historico_jogador2, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
                            diferenca1 = soma - tabuleiro_do_jogador2[dimensao_da_matriz][linha_coluna_tabuleiro]
                            if diferenca1 < 0:
                                diferenca1 *= -1
                    #condicional para indenticicar se eu vou manipular uma linha
                    else:
                        jogada = linha_coluna_tabuleiro
                        linha_coluna_tabuleiro = linha_coluna_tabuleiro.replace("L","")
                        linha_coluna_tabuleiro = int(linha_coluna_tabuleiro)
                        linha_coluna_indice.append(linha_coluna_tabuleiro)
                        #condicional para saber a vez do jogador 1
                        if vez_do_jogador == 1:
                            historico_jogador1 = historico_jo1(soma, historico_jogador1, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador1)
                            diferenca = soma - tabuleiro_do_jogador1[linha_coluna_tabuleiro][dimensao_da_matriz]
                            if diferenca < 0:
                                diferenca *= -1
                        #condicional para saber a vez do jogador 2
                        if vez_do_jogador == 2:
                            historico_jogador2 = historico_jo2(soma, historico_jogador2, dimensao_da_matriz, jogada, linha_coluna_tabuleiro, tabuleiro_do_jogador2)
                            diferenca1 = soma - tabuleiro_do_jogador2[linha_coluna_tabuleiro][dimensao_da_matriz]
                            if diferenca1 < 0:
                                diferenca1 *= -1

            #condicional para se a diferenca do primeiro jogador for menor que a diferenca do segundo jogador e se tem em comum um tabuleiro
            if diferenca < diferenca1 and tabuleiro_do_jogador2 == 0:
                indice_jo = 0
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)

            #condicional para se a diferenca do primeiro jogador for maior que a diferenca do segundo jogador e se tem em comum um tabuleiro    
            elif diferenca > diferenca1 and tabuleiro_do_jogador2 == 0:
                indice_jo = 1
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)
            
            #condicional para se a diferenca do primeiro jogador for igual a diferenca do segundo jogador e se tem em comum um tabuleiro
            elif diferenca == diferenca1 and tabuleiro_do_jogador2 == 0:
                indice_jo = 0
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)
                indice_jo = 1
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)

            #condicional para se a diferenca do primeiro jogador for menor que a diferenca do segundo jogador e se tem o tabuleiro1 e tabuleiro2
            elif diferenca < diferenca1 and tabuleiro_do_jogador2 != 0:
                indice_jo = 0
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)

            #condicional para se a diferenca do primeiro jogador for maior que a diferenca do segundo jogador e se tem o tabuleiro1 e tabuleiro2
            elif diferenca > diferenca1 and tabuleiro_do_jogador2 != 0:
                indice_jo = 1
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador2 = revelar_tab2(dificuldade, tabuleiro_vazio_do_jogador2, tabuleiro_do_jogador2, linha_coluna, somas, linha_coluna_tabuleiro, dimensao_da_matriz, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)
            
            #condicional para se a diferenca do primeiro jogado for igual a diferenca do segundo jogador e se tem o tabuleiro1 e tabuleiro2
            elif diferenca == diferenca1 and tabuleiro_do_jogador2 != 0:
                indice_jo = 0
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador1 = revelar_tab1(dificuldade, tabuleiro_vazio_do_jogador1, linha_coluna_tabuleiro, tabuleiro_do_jogador1, dimensao_da_matriz, somas, linha_coluna, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)
                indice_jo = 1
                vazios_inicial = indices_vazios_inicial(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2)
                linha_coluna_tabuleiro = linha_coluna_indice[indice_jo]
                tabuleiro_vazio_do_jogador2 = revelar_tab2(dificuldade, tabuleiro_vazio_do_jogador2, tabuleiro_do_jogador2, linha_coluna, somas, linha_coluna_tabuleiro, dimensao_da_matriz, indice_jo)
                pontos_jogador1, pontos_jogador2 = indices_vazios_final(dificuldade, indice_jo, tabuleiro_vazio_do_jogador1, tabuleiro_vazio_do_jogador2, pontos_jogador1, pontos_jogador2, vazios_inicial)

            #condicional para indentificar se e um historico
            if rodadas > 0:
                print("------------------------------Histórico------------------------------")
                if tabuleiro_vazio_do_jogador2 == 0:
                    #funcao para mostrar o historico dos jogadores
                    print("Histórico do {} e do {}:".format(jogador1, jogador2))
                    print(historico_jogador1)

                #condicional para indentificar se sao dois historicos
                else:
                    #funcao para mostrar o historico do primeiro jogador
                    print("Histórico do {}:".format(jogador1))
                    print(historico_jogador1)
                    print()
                    #funcao para mostrar o historico do segundo jogador
                    print("Histórico do {}:".format(jogador2))
                    print(historico_jogador2)
                print()
                print("---------------------------------------------------------------------")
            rodadas -=1 

    #condicionais para indentificar o vencedor
    if pontos_jogador1 > pontos_jogador2:
        #funcao para mostrar que o primeiro jogador venceu
        print("{} venceu!".format(jogador1))
    elif pontos_jogador1 < pontos_jogador2:
        #funcao para mostrar que o segundo jogador venceu
        print("{} venceu!".format(jogador2))
    else:
        #funcao para mostrar que o primeiro jogador e o segundo jogador empataram
        print("{} e {} empataram!".format(jogador1, jogador2))
if __name__ == '__main__':
    main()