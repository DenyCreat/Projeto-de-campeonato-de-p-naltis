import random
print('--------------------RODADA 1--------------------')
print('partida 1')
print('--casa--: time 1')
print('--visitante--: time 2')
a = 'X'
b = 'O'
lista = [a,b]
pt1 = 0
pt2 = 0
pt3 = 0
pt4 = 0
pt5 = 0
pt6 = 0
pt7 = 0
pt8 = 0
sgT1 = 0
sgT2 = 0
sgT3 = 0
sgT4 = 0
sgT5 = 0
sgT6 = 0
sgT7 = 0
sgT8 = 0
p1t1 = random.choice(lista)
p1t2 = random.choice(lista)
print('penalty 1 T1:', p1t1)
print('penalty 1 T2:', p1t2)
print('digite 0 para sair do jogo ou 1 para continuar')
s = int(input('digite o valor:' ))
if s == 0:
    print('fim do jogo')
    exit
if s != 0 and s != 1:
    print('valor inválido')
    print('fim do jogo')
    exit
elif s == 1:
    p2t1 = random.choice(lista)
    p2t2 = random.choice(lista)
    print('penalty 2 T1:', p2t1)
    print('penalty 2 T2:', p2t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p3t1 = random.choice(lista)
    p3t2 = random.choice(lista)
    print('penalty 3 T1:', p3t1)
    print('penalty 3 T2:', p3t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p4t1 = random.choice(lista)
    p4t2 = random.choice(lista)
    print('penalty 4 T1:', p4t1)
    print('penalty 4 T2:', p4t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p5t1 = random.choice(lista)
    p5t2 = random.choice(lista)
    print('penalty 5 T1:', p5t1)
    print('penalty 5 T2:', p5t2)
listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
print(listaPT1)
print(listaPT2)
print('o placar dos penaltis T1 é:', len(PpT1))
print('o placar dos penaltis T2 é:', len(PpT2))
if len(PpT1) > len(PpT2):
    print('time 1 ganhou o jogo, +3pts')
    pt1 = 3
    pt2 = 0
    sgT1 += len(PpT1)
    print('----------pontuacão atual do time 1 é:', pt1)
    print('----------pontuacão atual do time 2 é:', pt2)
elif len(PpT1) < len(PpT2):
    print('time 2 ganhou o jogo, +3pts')
    pt2 = 3
    pt1 = 0
    sgT2 += len(PpT2)
    print('----------pontuacão atual do time 2 é:', pt2)
    print('----------pontuacão atual do time 1 é:', pt1)
elif len(PpT1) == len(PpT2):
    print('agora é disputa nas alternadas, até alguem errar')
    p6t1 = random.choice(lista)
    p6t2 = random.choice(lista)
    print('penalty 6 T1:', p6t1)
    print('penalty 6 T2:', p6t2)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print('o placar dos penaltis T1 é:', len(PpT1))
    print('o placar dos penaltis T2 é:', len(PpT2))
    if len(PpT1) > len(PpT2):
        print('time 1 ganhou o jogo, +3pts')
        pt1 = 3
        pt2 = 0
        sgT1 += len(PpT1)
        print('----------pontuacão atual do time 1 é:', pt1)
        print('----------pontuacão atual do time 2 é:', pt2)
    elif len(PpT1) < len(PpT2):
        print('time 2 ganhou o jogo, +3pts')
        pt2 = 3
        pt1 = 0
        sgT2 += len(PpT2)
        print('----------pontuacão atual do time 2 é:', pt2)
        print('----------pontuacão atual do time 1 é:', pt1)
    elif len(PpT1) == len(PpT2):
        p7t1 = random.choice(lista)
        p7t2 = random.choice(lista)
        print('penalty 7 T1:', p7t1)
        print('penalty 7 T2:', p7t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print('o placar dos penaltis T1 é:', len(PpT1))
        print('o placar dos penaltis T2 é:', len(PpT2))
        if len(PpT1) > len(PpT2):
            print('time 1 ganhou o jogo, +3pts')
            pt1 = 3
            pt2 = 0
            sgT1 += len(PpT1)
            print('----------pontuacão atual do time 1 é:', pt1)
            print('----------pontuacão atual do time 2 é:', pt2)
        elif len(PpT1) < len(PpT2):
            print('time 2 ganhou o jogo, +3pts')
            pt2 = 3
            pt1 = 0
            sgT2 += len(PpT2)
            print('----------pontuacão atual do time 2 é:', pt2)
            print('----------pontuacão atual do time 1 é:', pt1)
        elif len(PpT1) == len(PpT2):
            p8t1 = random.choice(lista)
            p8t2 = random.choice(lista)
            print('penalty 8 T1:', p8t1)
            print('penalty 8 T2:', p8t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print('o placar dos penaltis T1 é:', len(PpT1))
            print('o placar dos penaltis T2 é:', len(PpT2))
            if len(PpT1) > len(PpT2):
                print('time 1 ganhou o jogo, +3pts')
                pt1 = 3
                pt2 = 0
                sgT1 += len(PpT1)
                print('----------pontuacão atual do time 1 é:', pt1)
                print('----------pontuacão atual do time 2 é:', pt2)
            elif len(PpT1) < len(PpT2):
                print('time 2 ganhou o jogo, +3pts')
                pt2 = 3
                pt1 = 0
                sgT2 += len(PpT2)
                print('----------pontuacão atual do time 2 é:', pt2)
                print('----------pontuacão atual do time 1 é:', pt1)
            elif len(PpT1) == len(PpT2):
                p9t1 = random.choice(lista)
                p9t2 = random.choice(lista)
                print('penalty 9 T1:', p9t1)
                print('penalty 9 T2:', p9t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print('o placar dos penaltis T1 é:', len(PpT1))
                print('o placar dos penaltis T2 é:', len(PpT2))
                if len(PpT1) > len(PpT2):
                    print('time 1 ganhou o jogo, +3pts')
                    pt1 = 3
                    pt2 = 0
                    sgT1 += len(PpT1)
                    print('----------pontuacão atual do time 1 é:', pt1)
                    print('----------pontuacão atual do time 2 é:', pt2)
                elif len(PpT1) < len(PpT2):
                    print('time 2 ganhou o jogo, +3pts')
                    pt2 = 3
                    pt1 = 0
                    sgT2 += len(PpT2)
                    print('----------pontuacão atual do time 2 é:', pt2)
                    print('----------pontuacão atual do time 1 é:', pt1)
                elif len(PpT1) == len(PpT2):
                    p10t1 = random.choice(lista)
                    p10t2 = random.choice(lista)
                    print('penalty 10 T1:', p10t1)
                    print('penalty 10 T2:', p10t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print('o placar dos penaltis T1 é:', len(PpT1))
                    print('o placar dos penaltis T2 é:', len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print('time 1 ganhou o jogo, +3pts')
                        pt1 = 3
                        pt2 = 0
                        sgT1 += len(PpT1)
                        print('----------pontuacão atual do time 1 é:', pt1)
                        print('----------pontuacão atual do time 2 é:', pt2)
                    elif len(PpT1) < len(PpT2):
                        print('time 2 ganhou o jogo, +3pts')
                        pt2 = 3
                        pt1 = 0
                        sgT2 += len(PpT2)
                        print('----------pontuacão atual do time 2 é:', pt2)
                        print('----------pontuacão atual do time 1 é:', pt1)
                    elif len(PpT1) == len(PpT2):
                        p11t1 = random.choice(lista)
                        p11t2 = random.choice(lista)
                        print('penalty 11 T1:', p11t1)
                        print('penalty 11 T2:', p11t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print('o placar dos penaltis T1 é:', len(PpT1))
                        print('o placar dos penaltis T2 é:', len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print('time 1 ganhou o jogo, +3pts')
                            pt1 = 3
                            pt2 = 0
                            sgT1 += len(PpT1)
                            print('----------pontuacão atual do time 1 é:', pt1)
                            print('----------pontuacão atual do time 2 é:', pt2)
                        elif len(PpT1) < len(PpT2):
                            print('time 2 ganhou o jogo, +3pts')
                            pt2 = 3
                            pt1 = 0
                            sgT2 += len(PpT2)
                            print('----------pontuacão atual do time 2 é:', pt2)
                            print('----------pontuacão atual do time 1 é:', pt1)
                        elif len(PpT1) == len(PpT2):
                            p12t1 = random.choice(lista)
                            p12t2 = random.choice(lista)
                            print('penalty 12 T1:', p12t1)
                            print('penalty 12 T2:', p12t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print('o placar dos penaltis T1 é:', len(PpT1))
                            print('o placar dos penaltis T2 é:', len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print('time 1 ganhou o jogo, +3pts')
                                pt1 = 3
                                pt2 = 0
                                sgT1 += len(PpT1)
                                print('----------pontuacão atual do time 1 é:', pt1)
                                print('----------pontuacão atual do time 2 é:', pt2)
                            elif len(PpT1) < len(PpT2):
                                print('time 2 ganhou o jogo, +3pts')
                                pt2 = 3
                                pt1 = 0
                                sgT2 += len(PpT2)
                                print('----------pontuacão atual do time 2 é:', pt2)
                                print('----------pontuacão atual do time 1 é:', pt1)
                            elif len(PpT1) == len(PpT2):
                                p13t1 = random.choice(lista)
                                p13t2 = random.choice(lista)
                                print('penalty 13 T1:', p13t1)
                                print('penalty 13 T2:', p13t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print('o placar dos penaltis T1 é:', len(PpT1))
                                print('o placar dos penaltis T2 é:', len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print('time 1 ganhou o jogo, +3pts')
                                    pt1 = 3
                                    pt2 = 0
                                    sgT1 += len(PpT1)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                    print('----------pontuacão atual do time 2 é:', pt2)
                                elif len(PpT1) < len(PpT2):
                                    print('time 2 ganhou o jogo, +3pts')
                                    pt2 = 3
                                    pt1 = 0
                                    sgT2 += len(PpT2)
                                    print('----------pontuacão atual do time 2 é:', pt2)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                elif len(PpT1) == len(PpT2):
                                    p14t1 = random.choice(lista)
                                    p14t2 = random.choice(lista)
                                    print('penalty 14 T1:', p14t1)
                                    print('penalty 14 T2:', p14t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print('o placar dos penaltis T1 é:', len(PpT1))
                                    print('o placar dos penaltis T2 é:', len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print('time 1 ganhou o jogo, +3pts')
                                        pt1 = 3
                                        pt2 = 0
                                        sgT1 += len(PpT1)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                        print('----------pontuacão atual do time 2 é:', pt2)
                                    elif len(PpT1) < len(PpT2):
                                        print('time 2 ganhou o jogo, +3pts')
                                        pt2 = 3
                                        pt1 = 0
                                        sgT2 += len(PpT2)
                                        print('----------pontuacão atual do time 2 é:', pt2)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                    elif len(PpT1) == len(PpT2):
                                        p15t1 = random.choice(lista)
                                        p15t2 = random.choice(lista)
                                        print('penalty 15 T1:', p15t1)
                                        print('penalty 15 T2:', p15t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print('o placar dos penaltis T1 é:', len(PpT1))
                                        print('o placar dos penaltis T2 é:', len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print('time 1 ganhou o jogo, +3pts')
                                            pt1 = 3
                                            pt2 = 0
                                            sgT1 += len(PpT1)
                                            print('----------pontuacão atual do time 1 é:', pt1)
                                            print('----------pontuacão atual do time 2 é:', pt2)
                                        elif len(PpT1) < len(PpT2):
                                            print('time 2 ganhou o jogo, +3pts')
                                            pt2 = 3
                                            pt1 = 0
                                            sgT2 += len(PpT2)
                                            print('----------pontuacão atual do time 2 é:', pt2)
                                            print('----------pontuacão atual do time 1 é:', pt1)


import random
print('--------------------RODADA 1--------------------')
print('partida 2')
print('--casa--: time 1')
print('--visitante--: time 3')
a = 'X'
b = 'O'
lista = [a,b]
p1t1 = random.choice(lista)
p1t2 = random.choice(lista)
print('penalty 1 T1:', p1t1)
print('penalty 1 T3:', p1t2)
print('digite 0 para sair do jogo ou 1 para continuar')
s = int(input('digite o valor:' ))
if s == 0:
    print('fim do jogo')
    exit
if s != 0 and s != 1:
    print('valor inválido')
    print('fim do jogo')
    exit
elif s == 1:
    p2t1 = random.choice(lista)
    p2t2 = random.choice(lista)
    print('penalty 2 T1:', p2t1)
    print('penalty 2 T3:', p2t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p3t1 = random.choice(lista)
    p3t2 = random.choice(lista)
    print('penalty 3 T1:', p3t1)
    print('penalty 3 T3:', p3t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p4t1 = random.choice(lista)
    p4t2 = random.choice(lista)
    print('penalty 4 T1:', p4t1)
    print('penalty 4 T3:', p4t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p5t1 = random.choice(lista)
    p5t2 = random.choice(lista)
    print('penalty 5 T1:', p5t1)
    print('penalty 5 T3:', p5t2)
listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
print(listaPT1)
print(listaPT2)
print('o placar dos penaltis T1 é:', len(PpT1))
print('o placar dos penaltis T3 é:', len(PpT2))
if len(PpT1) > len(PpT2):
    print('time 1 ganhou o jogo, +3pts')
    pt1 += 3
    pt3 += 0
    sgT1 += len(PpT1)
    print('----------pontuacão atual do time 1 é:', pt1)
    print('----------pontuacão atual do time 3 é:', pt3)
elif len(PpT1) < len(PpT2):
    print('time 3 ganhou o jogo, +3pts')
    pt3 += 3
    pt1 += 0
    sgT3 += len(PpT2)
    print('----------pontuacão atual do time 3 é:', pt3)
    print('----------pontuacão atual do time 1 é:', pt1)
elif len(PpT1) == len(PpT2):
    print('agora é disputa nas alternadas, até alguem errar')
    p6t1 = random.choice(lista)
    p6t2 = random.choice(lista)
    print('penalty 6 T1:', p6t1)
    print('penalty 6 T3:', p6t2)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print('o placar dos penaltis T1 é:', len(PpT1))
    print('o placar dos penaltis T3 é:', len(PpT2))
    if len(PpT1) > len(PpT2):
        print('time 1 ganhou o jogo, +3pts')
        pt1 += 3
        pt3 += 0
        sgT1 += len(PpT1)
        print('----------pontuacão atual do time 1 é:', pt1)
        print('----------pontuacão atual do time 3 é:', pt3)
    elif len(PpT1) < len(PpT2):
        print('time 3 ganhou o jogo, +3pts')
        pt3 += 3
        pt1 += 0
        sgT3 += len(PpT2)
        print('----------pontuacão atual do time 3 é:', pt3)
        print('----------pontuacão atual do time 1 é:', pt1)
    elif len(PpT1) == len(PpT2):
        p7t1 = random.choice(lista)
        p7t2 = random.choice(lista)
        print('penalty 7 T1:', p7t1)
        print('penalty 7 T3:', p7t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print('o placar dos penaltis T1 é:', len(PpT1))
        print('o placar dos penaltis T3 é:', len(PpT2))
        if len(PpT1) > len(PpT2):
            print('time 1 ganhou o jogo, +3pts')
            pt1 += 3
            pt3 += 0
            sgT1 += len(PpT1)
            print('----------pontuacão atual do time 1 é:', pt1)
            print('----------pontuacão atual do time 3 é:', pt3)
        elif len(PpT1) < len(PpT2):
            print('time 3 ganhou o jogo, +3pts')
            pt3 += 3
            pt1 += 0
            sgT3 += len(PpT2)
            print('----------pontuacão atual do time 3 é:', pt3)
            print('----------pontuacão atual do time 1 é:', pt1)
        elif len(PpT1) == len(PpT2):
            p8t1 = random.choice(lista)
            p8t2 = random.choice(lista)
            print('penalty 8 T1:', p8t1)
            print('penalty 8 T3:', p8t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print('o placar dos penaltis T1 é:', len(PpT1))
            print('o placar dos penaltis T3 é:', len(PpT2))
            if len(PpT1) > len(PpT2):
                print('time 1 ganhou o jogo, +3pts')
                pt1 += 3
                pt3 += 0
                sgT1 += len(PpT1)
                print('----------pontuacão atual do time 1 é:', pt1)
                print('----------pontuacão atual do time 3 é:', pt3)
            elif len(PpT1) < len(PpT2):
                print('time 3 ganhou o jogo, +3pts')
                pt3 += 3
                pt1 += 0
                sgT3 += len(PpT2)
                print('----------pontuacão atual do time 3 é:', pt3)
                print('----------pontuacão atual do time 1 é:', pt1)
            elif len(PpT1) == len(PpT2):
                p9t1 = random.choice(lista)
                p9t2 = random.choice(lista)
                print('penalty 9 T1:', p9t1)
                print('penalty 9 T3:', p9t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print('o placar dos penaltis T1 é:', len(PpT1))
                print('o placar dos penaltis T3 é:', len(PpT2))
                if len(PpT1) > len(PpT2):
                    print('time 1 ganhou o jogo, +3pts')
                    pt1 += 3
                    pt3 += 0
                    sgT1 += len(PpT1)
                    print('----------pontuacão atual do time 1 é:', pt1)
                    print('----------pontuacão atual do time 3 é:', pt3)
                elif len(PpT1) < len(PpT2):
                    print('time 3 ganhou o jogo, +3pts')
                    pt3 += 3
                    pt1 += 0
                    sgT3 += len(PpT2)
                    print('----------pontuacão atual do time 3 é:', pt3)
                    print('----------pontuacão atual do time 1 é:', pt1)
                elif len(PpT1) == len(PpT2):
                    p10t1 = random.choice(lista)
                    p10t2 = random.choice(lista)
                    print('penalty 10 T1:', p10t1)
                    print('penalty 10 T3:', p10t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print('o placar dos penaltis T1 é:', len(PpT1))
                    print('o placar dos penaltis T3 é:', len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print('time 1 ganhou o jogo, +3pts')
                        pt1 += 3
                        pt3 += 0
                        sgT1 += len(PpT1)
                        print('----------pontuacão atual do time 1 é:', pt1)
                        print('----------pontuacão atual do time 3 é:', pt3)
                    elif len(PpT1) < len(PpT2):
                        print('time 3 ganhou o jogo, +3pts')
                        pt3 += 3
                        pt1 += 0
                        sgT3 += len(PpT2)
                        print('----------pontuacão atual do time 3 é:', pt3)
                        print('----------pontuacão atual do time 1 é:', pt1)
                    elif len(PpT1) == len(PpT2):
                        p11t1 = random.choice(lista)
                        p11t2 = random.choice(lista)
                        print('penalty 11 T1:', p11t1)
                        print('penalty 11 T3:', p11t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print('o placar dos penaltis T1 é:', len(PpT1))
                        print('o placar dos penaltis T3 é:', len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print('time 1 ganhou o jogo, +3pts')
                            pt1 += 3
                            pt3 += 0
                            sgT1 += len(PpT1)
                            print('----------pontuacão atual do time 1 é:', pt1)
                            print('----------pontuacão atual do time 3 é:', pt3)
                        elif len(PpT1) < len(PpT2):
                            print('time 3 ganhou o jogo, +3pts')
                            pt3 += 3
                            pt1 += 0
                            sgT3 += len(PpT2)
                            print('----------pontuacão atual do time 3 é:', pt3)
                            print('----------pontuacão atual do time 1 é:', pt1)
                        elif len(PpT1) == len(PpT2):
                            p12t1 = random.choice(lista)
                            p12t2 = random.choice(lista)
                            print('penalty 12 T1:', p12t1)
                            print('penalty 12 T3:', p12t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print('o placar dos penaltis T1 é:', len(PpT1))
                            print('o placar dos penaltis T3 é:', len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print('time 1 ganhou o jogo, +3pts')
                                pt1 += 3
                                pt3 += 0
                                sgT1 += len(PpT1)
                                print('----------pontuacão atual do time 1 é:', pt1)
                                print('----------pontuacão atual do time 3 é:', pt3)
                            elif len(PpT1) < len(PpT2):
                                print('time 3 ganhou o jogo, +3pts')
                                pt3 += 3
                                pt1 += 0
                                sgT3 += len(PpT2)
                                print('----------pontuacão atual do time 3 é:', pt3)
                                print('----------pontuacão atual do time 1 é:', pt1)
                            elif len(PpT1) == len(PpT2):
                                p13t1 = random.choice(lista)
                                p13t2 = random.choice(lista)
                                print('penalty 13 T1:', p13t1)
                                print('penalty 13 T3:', p13t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print('o placar dos penaltis T1 é:', len(PpT1))
                                print('o placar dos penaltis T3 é:', len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print('time 1 ganhou o jogo, +3pts')
                                    pt1 += 3
                                    pt3 += 0
                                    sgT1 += len(PpT1)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                    print('----------pontuacão atual do time 3 é:', pt3)
                                elif len(PpT1) < len(PpT2):
                                    print('time 3 ganhou o jogo, +3pts')
                                    pt3 += 3
                                    pt1 += 0
                                    sgT3 += len(PpT2)
                                    print('----------pontuacão atual do time 3 é:', pt3)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                elif len(PpT1) == len(PpT2):
                                    p14t1 = random.choice(lista)
                                    p14t2 = random.choice(lista)
                                    print('penalty 14 T1:', p14t1)
                                    print('penalty 14 T3:', p14t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print('o placar dos penaltis T1 é:', len(PpT1))
                                    print('o placar dos penaltis T3 é:', len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print('time 1 ganhou o jogo, +3pts')
                                        pt1 += 3
                                        pt3 += 0
                                        sgT1 += len(PpT1)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                        print('----------pontuacão atual do time 3 é:', pt3)
                                    elif len(PpT1) < len(PpT2):
                                        print('time 3 ganhou o jogo, +3pts')
                                        pt3 += 3
                                        pt1 += 0
                                        sgT3 += len(PpT2)
                                        print('----------pontuacão atual do time 3 é:', pt3)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                    elif len(PpT1) == len(PpT2):
                                        p15t1 = random.choice(lista)
                                        p15t2 = random.choice(lista)
                                        print('penalty 15 T1:', p15t1)
                                        print('penalty 15 T3:', p15t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print('o placar dos penaltis T1 é:', len(PpT1))
                                        print('o placar dos penaltis T3 é:', len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print('time 1 ganhou o jogo, +3pts')
                                            pt1 += 3
                                            pt3 += 0
                                            sgT1 += len(PpT1)
                                            print('----------pontuacão atual do time 1 é:', pt1)
                                            print('----------pontuacão atual do time 3 é:', pt3)
                                        elif len(PpT1) < len(PpT2):
                                            print('time 3 ganhou o jogo, +3pts')
                                            pt3 += 3
                                            pt1 += 0
                                            sgT3 += len(PpT2)
                                            print('----------pontuacão atual do time 3 é:', pt3)
                                            print('----------pontuacão atual do time 1 é:', pt1)


import random
print('--------------------RODADA 1--------------------')
print('partida 3')
print('--casa--: time 1')
print('--visitante--: time 4')
a = 'X'
b = 'O'
lista = [a,b]
p1t1 = random.choice(lista)
p1t2 = random.choice(lista)
print('penalty 1 T1:', p1t1)
print('penalty 1 T4:', p1t2)
print('digite 0 para sair do jogo ou 1 para continuar')
s = int(input('digite o valor:' ))
if s == 0:
    print('fim do jogo')
    exit
if s != 0 and s != 1:
    print('valor inválido')
    print('fim do jogo')
    exit
elif s == 1:
    p2t1 = random.choice(lista)
    p2t2 = random.choice(lista)
    print('penalty 2 T1:', p2t1)
    print('penalty 2 T4:', p2t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p3t1 = random.choice(lista)
    p3t2 = random.choice(lista)
    print('penalty 3 T1:', p3t1)
    print('penalty 3 T4:', p3t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p4t1 = random.choice(lista)
    p4t2 = random.choice(lista)
    print('penalty 4 T1:', p4t1)
    print('penalty 4 T4:', p4t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p5t1 = random.choice(lista)
    p5t2 = random.choice(lista)
    print('penalty 5 T1:', p5t1)
    print('penalty 5 T4:', p5t2)
listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
print(listaPT1)
print(listaPT2)
print('o placar dos penaltis T1 é:', len(PpT1))
print('o placar dos penaltis T4 é:', len(PpT2))
if len(PpT1) > len(PpT2):
    print('time 1 ganhou o jogo, +3pts')
    pt1 += 3
    pt4 += 0
    sgT1 += len(PpT1)
    print('----------pontuacão atual do time 1 é:', pt1)
    print('----------pontuacão atual do time 4 é:', pt4)
elif len(PpT1) < len(PpT2):
    print('time 4 ganhou o jogo, +3pts')
    pt4 += 3
    pt1 += 0
    sgT4 += len(PpT2)
    print('----------pontuacão atual do time 4 é:', pt4)
    print('----------pontuacão atual do time 1 é:', pt1)
elif len(PpT1) == len(PpT2):
    print('agora é disputa nas alternadas, até alguem errar')
    p6t1 = random.choice(lista)
    p6t2 = random.choice(lista)
    print('penalty 6 T1:', p6t1)
    print('penalty 6 T4:', p6t2)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print('o placar dos penaltis T1 é:', len(PpT1))
    print('o placar dos penaltis T4 é:', len(PpT2))
    if len(PpT1) > len(PpT2):
        print('time 1 ganhou o jogo, +3pts')
        pt1 += 3
        pt4 += 0
        sgT1 += len(PpT1)
        print('----------pontuacão atual do time 1 é:', pt1)
        print('----------pontuacão atual do time 4 é:', pt4)
    elif len(PpT1) < len(PpT2):
        print('time 4 ganhou o jogo, +3pts')
        pt4 += 3
        pt1 += 0
        sgT4 += len(PpT2)
        print('----------pontuacão atual do time 4 é:', pt4)
        print('----------pontuacão atual do time 1 é:', pt1)
    elif len(PpT1) == len(PpT2):
        p7t1 = random.choice(lista)
        p7t2 = random.choice(lista)
        print('penalty 7 T1:', p7t1)
        print('penalty 7 T4:', p7t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print('o placar dos penaltis T1 é:', len(PpT1))
        print('o placar dos penaltis T4 é:', len(PpT2))
        if len(PpT1) > len(PpT2):
            print('time 1 ganhou o jogo, +3pts')
            pt1 += 3
            pt4 += 0
            sgT1 += len(PpT1)
            print('----------pontuacão atual do time 1 é:', pt1)
            print('----------pontuacão atual do time 4 é:', pt4)
        elif len(PpT1) < len(PpT2):
            print('time 4 ganhou o jogo, +3pts')
            pt4 += 3
            pt1 += 0
            sgT4 += len(PpT2)
            print('----------pontuacão atual do time 4 é:', pt4)
            print('----------pontuacão atual do time 1 é:', pt1)
        elif len(PpT1) == len(PpT2):
            p8t1 = random.choice(lista)
            p8t2 = random.choice(lista)
            print('penalty 8 T1:', p8t1)
            print('penalty 8 T4:', p8t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print('o placar dos penaltis T1 é:', len(PpT1))
            print('o placar dos penaltis T4 é:', len(PpT2))
            if len(PpT1) > len(PpT2):
                print('time 1 ganhou o jogo, +3pts')
                pt1 += 3
                pt4 += 0
                sgT1 += len(PpT1)
                print('----------pontuacão atual do time 1 é:', pt1)
                print('----------pontuacão atual do time 4 é:', pt4)
            elif len(PpT1) < len(PpT2):
                print('time 4 ganhou o jogo, +3pts')
                pt4 += 3
                pt1 += 0
                sgT4 += len(PpT2)
                print('----------pontuacão atual do time 4 é:', pt4)
                print('----------pontuacão atual do time 1 é:', pt1)
            elif len(PpT1) == len(PpT2):
                p9t1 = random.choice(lista)
                p9t2 = random.choice(lista)
                print('penalty 9 T1:', p9t1)
                print('penalty 9 T4:', p9t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print('o placar dos penaltis T1 é:', len(PpT1))
                print('o placar dos penaltis T4 é:', len(PpT2))
                if len(PpT1) > len(PpT2):
                    print('time 1 ganhou o jogo, +3pts')
                    pt1 += 3
                    pt4 += 0
                    sgT1 += len(PpT1)
                    print('----------pontuacão atual do time 1 é:', pt1)
                    print('----------pontuacão atual do time 4 é:', pt4)
                elif len(PpT1) < len(PpT2):
                    print('time 4 ganhou o jogo, +3pts')
                    pt4 += 3
                    pt1 += 0
                    sgT4 += len(PpT2)
                    print('----------pontuacão atual do time 4 é:', pt4)
                    print('----------pontuacão atual do time 1 é:', pt1)
                elif len(PpT1) == len(PpT2):
                    p10t1 = random.choice(lista)
                    p10t2 = random.choice(lista)
                    print('penalty 10 T1:', p10t1)
                    print('penalty 10 T4:', p10t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print('o placar dos penaltis T1 é:', len(PpT1))
                    print('o placar dos penaltis T4 é:', len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print('time 1 ganhou o jogo, +3pts')
                        pt1 += 3
                        pt4 += 0
                        sgT1 += len(PpT1)
                        print('----------pontuacão atual do time 1 é:', pt1)
                        print('----------pontuacão atual do time 4 é:', pt4)
                    elif len(PpT1) < len(PpT2):
                        print('time 4 ganhou o jogo, +3pts')
                        pt4 += 3
                        pt1 += 0
                        sgT4 += len(PpT2)
                        print('----------pontuacão atual do time 4 é:', pt4)
                        print('----------pontuacão atual do time 1 é:', pt1)
                    elif len(PpT1) == len(PpT2):
                        p11t1 = random.choice(lista)
                        p11t2 = random.choice(lista)
                        print('penalty 11 T1:', p11t1)
                        print('penalty 11 T4:', p11t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print('o placar dos penaltis T1 é:', len(PpT1))
                        print('o placar dos penaltis T4 é:', len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print('time 1 ganhou o jogo, +3pts')
                            pt1 += 3
                            pt4 += 0
                            sgT1 += len(PpT1)
                            print('----------pontuacão atual do time 1 é:', pt1)
                            print('----------pontuacão atual do time 4 é:', pt4)
                        elif len(PpT1) < len(PpT2):
                            print('time 4 ganhou o jogo, +3pts')
                            pt4 += 3
                            pt1 += 0
                            sgT4 += len(PpT2)
                            print('----------pontuacão atual do time 4 é:', pt4)
                            print('----------pontuacão atual do time 1 é:', pt1)
                        elif len(PpT1) == len(PpT2):
                            p12t1 = random.choice(lista)
                            p12t2 = random.choice(lista)
                            print('penalty 12 T1:', p12t1)
                            print('penalty 12 T4:', p12t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print('o placar dos penaltis T1 é:', len(PpT1))
                            print('o placar dos penaltis T4 é:', len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print('time 1 ganhou o jogo, +3pts')
                                pt1 += 3
                                pt4 += 0
                                sgT1 += len(PpT1)
                                print('----------pontuacão atual do time 1 é:', pt1)
                                print('----------pontuacão atual do time 4 é:', pt4)
                            elif len(PpT1) < len(PpT2):
                                print('time 4 ganhou o jogo, +3pts')
                                pt4 += 3
                                pt1 += 0
                                sgT4 += len(PpT2)
                                print('----------pontuacão atual do time 4 é:', pt4)
                                print('----------pontuacão atual do time 1 é:', pt1)
                            elif len(PpT1) == len(PpT2):
                                p13t1 = random.choice(lista)
                                p13t2 = random.choice(lista)
                                print('penalty 13 T1:', p13t1)
                                print('penalty 13 T4:', p13t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print('o placar dos penaltis T1 é:', len(PpT1))
                                print('o placar dos penaltis T4 é:', len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print('time 1 ganhou o jogo, +3pts')
                                    pt1 += 3
                                    pt4 += 0
                                    sgT1 += len(PpT1)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                    print('----------pontuacão atual do time 4 é:', pt4)
                                elif len(PpT1) < len(PpT2):
                                    print('time 4 ganhou o jogo, +3pts')
                                    pt4 += 3
                                    pt1 += 0
                                    sgT4 += len(PpT2)
                                    print('----------pontuacão atual do time 4 é:', pt4)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                elif len(PpT1) == len(PpT2):
                                    p14t1 = random.choice(lista)
                                    p14t2 = random.choice(lista)
                                    print('penalty 14 T1:', p14t1)
                                    print('penalty 14 T4:', p14t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print('o placar dos penaltis T1 é:', len(PpT1))
                                    print('o placar dos penaltis T4 é:', len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print('time 1 ganhou o jogo, +3pts')
                                        pt1 += 3
                                        pt4 += 0
                                        sgT1 += len(PpT1)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                        print('----------pontuacão atual do time 4 é:', pt4)
                                    elif len(PpT1) < len(PpT2):
                                        print('time 4 ganhou o jogo, +3pts')
                                        pt4 += 3
                                        pt1 += 0
                                        sgT4 += len(PpT2)
                                        print('----------pontuacão atual do time 4 é:', pt4)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                    elif len(PpT1) == len(PpT2):
                                        p15t1 = random.choice(lista)
                                        p15t2 = random.choice(lista)
                                        print('penalty 15 T1:', p15t1)
                                        print('penalty 15 T4:', p15t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print('o placar dos penaltis T1 é:', len(PpT1))
                                        print('o placar dos penaltis T4 é:', len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print('time 1 ganhou o jogo, +3pts')
                                            pt1 += 3
                                            pt4 += 0
                                            sgT1 += len(PpT1)
                                            print('----------pontuacão atual do time 1 é:', pt1)
                                            print('----------pontuacão atual do time 4 é:', pt4)
                                        elif len(PpT1) < len(PpT2):
                                            print('time 4 ganhou o jogo, +3pts')
                                            pt4 += 3
                                            pt1 += 0
                                            sgT4 += len(PpT2)
                                            print('----------pontuacão atual do time 4 é:', pt4)
                                            print('----------pontuacão atual do time 1 é:', pt1)


import random
print('--------------------RODADA 1--------------------')
print('partida 4')
print('--casa--: time 1')
print('--visitante--: time 5')
a = 'X'
b = 'O'
lista = [a,b]
p1t1 = random.choice(lista)
p1t2 = random.choice(lista)
print('penalty 1 T1:', p1t1)
print('penalty 1 T5:', p1t2)
print('digite 0 para sair do jogo ou 1 para continuar')
s = int(input('digite o valor:' ))
if s == 0:
    print('fim do jogo')
    exit
if s != 0 and s != 1:
    print('valor inválido')
    print('fim do jogo')
    exit
elif s == 1:
    p2t1 = random.choice(lista)
    p2t2 = random.choice(lista)
    print('penalty 2 T1:', p2t1)
    print('penalty 2 T5:', p2t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p3t1 = random.choice(lista)
    p3t2 = random.choice(lista)
    print('penalty 3 T1:', p3t1)
    print('penalty 3 T5:', p3t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p4t1 = random.choice(lista)
    p4t2 = random.choice(lista)
    print('penalty 4 T1:', p4t1)
    print('penalty 4 T5:', p4t2)
s = int(input('digite 1 para proxima rodada de penaltis:' ))
if s != 1:
    print('fim do jogo')
    exit
else:
    p5t1 = random.choice(lista)
    p5t2 = random.choice(lista)
    print('penalty 5 T1:', p5t1)
    print('penalty 5 T5:', p5t2)
listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
print(listaPT1)
print(listaPT2)
print('o placar dos penaltis T1 é:', len(PpT1))
print('o placar dos penaltis T5 é:', len(PpT2))
if len(PpT1) > len(PpT2):
    print('time 1 ganhou o jogo, +3pts')
    pt1 += 3
    pt5 += 0
    sgT1 += len(PpT1)
    print('----------pontuacão atual do time 1 é:', pt1)
    print('----------pontuacão atual do time 5 é:', pt5)
elif len(PpT1) < len(PpT2):
    print('time 5 ganhou o jogo, +3pts')
    pt5 += 3
    pt1 += 0
    sgT5 += len(PpT2)
    print('----------pontuacão atual do time 5 é:', pt5)
    print('----------pontuacão atual do time 1 é:', pt1)
elif len(PpT1) == len(PpT2):
    print('agora é disputa nas alternadas, até alguem errar')
    p6t1 = random.choice(lista)
    p6t2 = random.choice(lista)
    print('penalty 6 T1:', p6t1)
    print('penalty 6 T5:', p6t2)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print('o placar dos penaltis T1 é:', len(PpT1))
    print('o placar dos penaltis T5 é:', len(PpT2))
    if len(PpT1) > len(PpT2):
        print('time 1 ganhou o jogo, +3pts')
        pt1 += 3
        pt5 += 0
        sgT1 += len(PpT1)
        print('----------pontuacão atual do time 1 é:', pt1)
        print('----------pontuacão atual do time 5 é:', pt5)
    elif len(PpT1) < len(PpT2):
        print('time 5 ganhou o jogo, +3pts')
        pt5 += 3
        pt1 += 0
        sgT5 += len(PpT2)
        print('----------pontuacão atual do time 5 é:', pt5)
        print('----------pontuacão atual do time 1 é:', pt1)
    elif len(PpT1) == len(PpT2):
        p7t1 = random.choice(lista)
        p7t2 = random.choice(lista)
        print('penalty 7 T1:', p7t1)
        print('penalty 7 T5:', p7t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print('o placar dos penaltis T1 é:', len(PpT1))
        print('o placar dos penaltis T5 é:', len(PpT2))
        if len(PpT1) > len(PpT2):
            print('time 1 ganhou o jogo, +3pts')
            pt1 += 3
            pt5 += 0
            sgT1 += len(PpT1)
            print('----------pontuacão atual do time 1 é:', pt1)
            print('----------pontuacão atual do time 5 é:', pt5)
        elif len(PpT1) < len(PpT2):
            print('time 5 ganhou o jogo, +3pts')
            pt5 += 3
            pt1 += 0
            sgT5 += len(PpT2)
            print('----------pontuacão atual do time 5 é:', pt5)
            print('----------pontuacão atual do time 1 é:', pt1)
        elif len(PpT1) == len(PpT2):
            p8t1 = random.choice(lista)
            p8t2 = random.choice(lista)
            print('penalty 8 T1:', p8t1)
            print('penalty 8 T5:', p8t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print('o placar dos penaltis T1 é:', len(PpT1))
            print('o placar dos penaltis T5 é:', len(PpT2))
            if len(PpT1) > len(PpT2):
                print('time 1 ganhou o jogo, +3pts')
                pt1 += 3
                pt5 += 0
                sgT1 += len(PpT1)
                print('----------pontuacão atual do time 1 é:', pt1)
                print('----------pontuacão atual do time 5 é:', pt5)
            elif len(PpT1) < len(PpT2):
                print('time 5 ganhou o jogo, +3pts')
                pt5 += 3
                pt1 += 0
                sgT5 += len(PpT2)
                print('----------pontuacão atual do time 5 é:', pt5)
                print('----------pontuacão atual do time 1 é:', pt1)
            elif len(PpT1) == len(PpT2):
                p9t1 = random.choice(lista)
                p9t2 = random.choice(lista)
                print('penalty 9 T1:', p9t1)
                print('penalty 9 T5:', p9t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print('o placar dos penaltis T1 é:', len(PpT1))
                print('o placar dos penaltis T5 é:', len(PpT2))
                if len(PpT1) > len(PpT2):
                    print('time 1 ganhou o jogo, +3pts')
                    pt1 += 3
                    pt5 += 0
                    sgT1 += len(PpT1)
                    print('----------pontuacão atual do time 1 é:', pt1)
                    print('----------pontuacão atual do time 5 é:', pt5)
                elif len(PpT1) < len(PpT2):
                    print('time 5 ganhou o jogo, +3pts')
                    pt5 += 3
                    pt1 += 0
                    sgT5 += len(PpT2)
                    print('----------pontuacão atual do time 5 é:', pt5)
                    print('----------pontuacão atual do time 1 é:', pt1)
                elif len(PpT1) == len(PpT2):
                    p10t1 = random.choice(lista)
                    p10t2 = random.choice(lista)
                    print('penalty 10 T1:', p10t1)
                    print('penalty 10 T5:', p10t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print('o placar dos penaltis T1 é:', len(PpT1))
                    print('o placar dos penaltis T5 é:', len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print('time 1 ganhou o jogo, +3pts')
                        pt1 += 3
                        pt5 += 0
                        sgT1 += len(PpT1)
                        print('----------pontuacão atual do time 1 é:', pt1)
                        print('----------pontuacão atual do time 5 é:', pt5)
                    elif len(PpT1) < len(PpT2):
                        print('time 5 ganhou o jogo, +3pts')
                        pt5 += 3
                        pt1 += 0
                        sgT5 += len(PpT2)
                        print('----------pontuacão atual do time 5 é:', pt5)
                        print('----------pontuacão atual do time 1 é:', pt1)
                    elif len(PpT1) == len(PpT2):
                        p11t1 = random.choice(lista)
                        p11t2 = random.choice(lista)
                        print('penalty 11 T1:', p11t1)
                        print('penalty 11 T5:', p11t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print('o placar dos penaltis T1 é:', len(PpT1))
                        print('o placar dos penaltis T5 é:', len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print('time 1 ganhou o jogo, +3pts')
                            pt1 += 3
                            pt5 += 0
                            sgT1 += len(PpT1)
                            print('----------pontuacão atual do time 1 é:', pt1)
                            print('----------pontuacão atual do time 5 é:', pt5)
                        elif len(PpT1) < len(PpT2):
                            print('time 5 ganhou o jogo, +3pts')
                            pt5 += 3
                            pt1 += 0
                            sgT5 += len(PpT2)
                            print('----------pontuacão atual do time 5 é:', pt5)
                            print('----------pontuacão atual do time 1 é:', pt1)
                        elif len(PpT1) == len(PpT2):
                            p12t1 = random.choice(lista)
                            p12t2 = random.choice(lista)
                            print('penalty 12 T1:', p12t1)
                            print('penalty 12 T5:', p12t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print('o placar dos penaltis T1 é:', len(PpT1))
                            print('o placar dos penaltis T5 é:', len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print('time 1 ganhou o jogo, +3pts')
                                pt1 += 3
                                pt5 += 0
                                sgT1 += len(PpT1)
                                print('----------pontuacão atual do time 1 é:', pt1)
                                print('----------pontuacão atual do time 5 é:', pt5)
                            elif len(PpT1) < len(PpT2):
                                print('time 5 ganhou o jogo, +3pts')
                                pt5 += 3
                                pt1 += 0
                                sgT5 += len(PpT2)
                                print('----------pontuacão atual do time 5 é:', pt5)
                                print('----------pontuacão atual do time 1 é:', pt1)
                            elif len(PpT1) == len(PpT2):
                                p13t1 = random.choice(lista)
                                p13t2 = random.choice(lista)
                                print('penalty 13 T1:', p13t1)
                                print('penalty 13 T5:', p13t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print('o placar dos penaltis T1 é:', len(PpT1))
                                print('o placar dos penaltis T5 é:', len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print('time 1 ganhou o jogo, +3pts')
                                    pt1 += 3
                                    pt5 += 0
                                    sgT1 += len(PpT1)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                    print('----------pontuacão atual do time 5 é:', pt5)
                                elif len(PpT1) < len(PpT2):
                                    print('time 5 ganhou o jogo, +3pts')
                                    pt5 += 3
                                    pt1 += 0
                                    sgT5 += len(PpT2)
                                    print('----------pontuacão atual do time 5 é:', pt5)
                                    print('----------pontuacão atual do time 1 é:', pt1)
                                elif len(PpT1) == len(PpT2):
                                    p14t1 = random.choice(lista)
                                    p14t2 = random.choice(lista)
                                    print('penalty 14 T1:', p14t1)
                                    print('penalty 14 T5:', p14t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print('o placar dos penaltis T1 é:', len(PpT1))
                                    print('o placar dos penaltis T5 é:', len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print('time 1 ganhou o jogo, +3pts')
                                        pt1 += 3
                                        pt5 += 0
                                        sgT1 += len(PpT1)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                        print('----------pontuacão atual do time 5 é:', pt5)
                                    elif len(PpT1) < len(PpT2):
                                        print('time 5 ganhou o jogo, +3pts')
                                        pt5 += 3
                                        pt1 += 0
                                        sgT5 += len(PpT2)
                                        print('----------pontuacão atual do time 5 é:', pt4)
                                        print('----------pontuacão atual do time 1 é:', pt1)
                                    elif len(PpT1) == len(PpT2):
                                        p15t1 = random.choice(lista)
                                        p15t2 = random.choice(lista)
                                        print('penalty 15 T1:', p15t1)
                                        print('penalty 15 T5:', p15t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print('o placar dos penaltis T1 é:', len(PpT1))
                                        print('o placar dos penaltis T5 é:', len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print('time 1 ganhou o jogo, +3pts')
                                            pt1 += 3
                                            pt5 += 0
                                            sgT1 += len(PpT1)
                                            print('----------pontuacão atual do time 1 é:', pt1)
                                            print('----------pontuacão atual do time 5 é:', pt5)
                                        elif len(PpT1) < len(PpT2):
                                            print('time 4 ganhou o jogo, +3pts')
                                            pt5 += 3
                                            pt1 += 0
                                            sgT5 += len(PpT2)
                                            print('----------pontuacão atual do time 5 é:', pt5)
                                            print('----------pontuacão atual do time 1 é:', pt1)


print('--------------------PONTUAÇÃO FINAL RODADA 1--------------------')

print('PONTUAÇÃO ATUAL')

d = {'----------pontuacão atual do time 1 é:':pt1, '----------pontuacão atual do time 2 é:':pt2, '----------pontuacão atual do time 3 é:':pt3, '----------pontuacão atual do time 4 é:':pt4, '----------pontuacão atual do time 5 é:':pt5, '----------pontuacão atual do time 6 é:':pt6, '----------pontuacão atual do time 7 é:':pt7, '----------pontuacão atual do time 8 é:':pt8 }
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', pt1, sgT1), ('time 2', pt2, sgT2), ('time 3', pt3, sgT3), ('time 4', pt4, sgT4), ('time 5', pt5, sgT5), ('time 6', pt6, sgT6), ('time 7', pt7, sgT7), ('time 8', pt8, sgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)
