from pulp import *
# pulp.pulpTestAll()
#DC = Data Center
#PPT = 
#Váriaveis de CUSTO por GB entre DC(i) e PPT(j)!!!
c_1_1 = 100
c_1_2 = 150
c_1_3 = 225
c_2_1 = 125
c_2_2 = 100
c_2_3 = 225
#Capacidades dos PPT(j)!!!
b_1 = 10000
b_2 = 15000
b_3 = 21000
#Tráfego dos DC(i) em GB!
d_1 = 16000
d_2 = 12000

prob = LpProblem(name="2_DCs_e_3PTTs",sense=LpMinimize) #cria o objeto do problema
#Variáveis de decisão
#LpContinuous = número Real!!
x_1_1 = LpVariable(name="X_DC_1_PPT_1",lowBound=0,upBound=None,cat=LpContinuous)
x_1_2 = LpVariable(name="X_DC_1_PPT_2",lowBound=0,upBound=None,cat=LpContinuous)
x_1_3 = LpVariable(name="X_DC_1_PPT_3",lowBound=0,upBound=None,cat=LpContinuous)
x_2_1 = LpVariable(name="X_DC_2_PPT_1",lowBound=0,upBound=None,cat=LpContinuous)
x_2_2 = LpVariable(name="X_DC_2_PPT_2",lowBound=0,upBound=None,cat=LpContinuous)
x_2_3 = LpVariable(name="X_DC_2_PPT_3",lowBound=0,upBound=None,cat=LpContinuous)

#Primeira a ser concatenada é a Função Objetivo!!
#Função Objetivo = c_1_1*x_1_1 + c_1_2*x_1_2 + c_1_3*x_1_3 + c_2_1*x_2_1 + c_2_2*x_2_2 + c_2_3*x_2_3
prob += c_1_1*x_1_1 + c_1_2*x_1_2 + c_1_3*x_1_3 + c_2_1*x_2_1 + c_2_2*x_2_2 + c_2_3*x_2_3, "Custo"
#Depois da função objetivo são concatenadas as restrições!
prob += x_1_1 + x_2_1 <= b_1,"Capacidade_PPT_1"
prob += x_1_2 + x_2_2 <= b_2,"Capacidade_PPT_2"
prob += x_1_3 + x_2_3 <= b_3,"Capacidade_PPT_3"
prob += x_1_1 + x_1_2 + x_1_3 == d_1,"Trafego_DC_1"
prob += x_2_1 + x_2_2 + x_2_3 == d_2,"Trafego_DC_2"

#Gera o arquivo do problema no Formato LP e salva no msm diretório
prob.writeLP("DC_PPT.lp")
#Resolve
prob.solve()
#Printa o status do problema. Optimal -> Solução ótima encontrada!, Infeasible -> Problema Impossível!
print("Status:", LpStatus[prob.status])
#Printa as váriaveis Resolvidas
for v in prob.variables():
    print(v.name,"=",v.varValue)
#Printa o custo Total da função Objetivo
print("O Custao total da infraestrutura eh= ",value(prob.objective))






