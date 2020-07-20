\* DCs_e_PTTs_generico *\
Minimize
Custo: 100 X_DC_1_PTT_1 + 150 X_DC_1_PTT_2 + 225 X_DC_1_PTT_3
 + 125 X_DC_2_PTT_1 + 100 X_DC_2_PTT_2 + 225 X_DC_2_PTT_3
Subject To
Capacidade_PTT_1: X_DC_1_PTT_1 + X_DC_2_PTT_1 <= 10000
Capacidade_PTT_2: X_DC_1_PTT_2 + X_DC_2_PTT_2 <= 15000
Capacidade_PTT_3: X_DC_1_PTT_3 + X_DC_2_PTT_3 <= 21000
Trafego_DC_1: X_DC_1_PTT_1 + X_DC_1_PTT_2 + X_DC_1_PTT_3 = 16000
Trafego_DC_2: X_DC_2_PTT_1 + X_DC_2_PTT_2 + X_DC_2_PTT_3 = 12000
End
