\* Minimizar_Atraso_Max_DCs_PPTs *\
Minimize
Custo: 5 X_DC_1_PTT_1 + 15 X_DC_1_PTT_2 + 10 X_DC_1_PTT_3 + 20 X_DC_2_PTT_1
 + 8 X_DC_2_PTT_2 + 10 X_DC_2_PTT_3
Subject To
Capacidade_PTT_1: 16000 X_DC_1_PTT_1 + 12000 X_DC_2_PTT_1 <= 20000
Capacidade_PTT_2: 16000 X_DC_1_PTT_2 + 12000 X_DC_2_PTT_2 <= 15000
Capacidade_PTT_3: 16000 X_DC_1_PTT_3 + 12000 X_DC_2_PTT_3 <= 21000
Restricao_1PPTporDC_DC_1: X_DC_1_PTT_1 + X_DC_1_PTT_2 + X_DC_1_PTT_3 = 1
Restricao_1PPTporDC_DC_2: X_DC_2_PTT_1 + X_DC_2_PTT_2 + X_DC_2_PTT_3 = 1
Variavel_ativacao_PTT_PTT_1: - X_DC_1_PTT_1 - X_DC_2_PTT_1 + Y_PTT_1 >= 0
Variavel_ativacao_PTT_PTT_2: - X_DC_1_PTT_2 - X_DC_2_PTT_2 + Y_PTT_2 >= 0
Variavel_ativacao_PTT_PTT_3: - X_DC_1_PTT_3 - X_DC_2_PTT_3 + Y_PTT_3 >= 0
restricoes_atrasos_DC_1_PTT_1: 5 X_DC_1_PTT_1 <= 5
restricoes_atrasos_DC_1_PTT_2: 15 X_DC_1_PTT_2 <= 15
restricoes_atrasos_DC_1_PTT_3: 10 X_DC_1_PTT_3 <= 10
restricoes_atrasos_DC_2_PTT_1: 20 X_DC_2_PTT_1 <= 20
restricoes_atrasos_DC_2_PTT_2: 8 X_DC_2_PTT_2 <= 8
restricoes_atrasos_DC_2_PTT_3: 10 X_DC_2_PTT_3 <= 10
Bounds
0 <= X_DC_1_PTT_1
0 <= X_DC_1_PTT_2
0 <= X_DC_1_PTT_3
0 <= X_DC_2_PTT_1
0 <= X_DC_2_PTT_2
0 <= X_DC_2_PTT_3
0 <= Y_PTT_1
0 <= Y_PTT_2
0 <= Y_PTT_3
Generals
X_DC_1_PTT_1
X_DC_1_PTT_2
X_DC_1_PTT_3
X_DC_2_PTT_1
X_DC_2_PTT_2
X_DC_2_PTT_3
Y_PTT_1
Y_PTT_2
Y_PTT_3
End
