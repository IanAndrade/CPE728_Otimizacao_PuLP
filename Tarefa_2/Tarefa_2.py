# Tarefa 2: Facility Location - p-center
# Autor: Ian Henriques de Andrade
#Objetivo: Formule um problema de otimizacão que minimize o maior atraso possével da infraestrutura (isto é, que possua a mesma
# funcão objetivo do problema p-center), considerando as exigências apresentadas.
#Exigencias:
#a) Todo o tráfego d(i) deverá ser escoado
#b) As capacidades de b(j) deverão ser respeitadas
#c) Um DC deve ser atendido por apenas um PTT
#d) Um PTT pode receber tráfego de vários DCs
#e) O custo total não poderá exceder o orçamento total (H)

from pulp import*
#Lista de DCs
dcList = ["DC_1","DC_2"]
#Tráfego em GB que deverá ser escoado do dos DC(i)
trafegoDCs = {"DC_1":16000,"DC_2":12000} #Dicionário!!

#Lista de PTTs
pttList = ["PTT_1","PTT_2","PTT_3"]
#Capacidade em GB dos PTT(j)
capPtts = {"PTT_1":20000,"PTT_2":15000,"PTT_3":21000} #Dicionário!!

#Matriz de Custos Variaveis (por GB): Cada linha é um DC e cada coluna é um PTT!!
matrizCustos_variaveis = [[100,150,225],[125,100,225]] #Ex: 125 é o custo do DC_2 e PTT1
#Transforma a matriz de Custos Variaveis em um dicionário de custos Variaveis!! (Facilita a definição do prob)
custos = makeDict([dcList,pttList],matrizCustos_variaveis,0)

#Matriz de Custos Fixos (Caso o PTT seja ativado).
custoAtivacaoPtts = {"PTT_1":1000,"PTT_2":2000,"PTT_3":3000} #Dicionário!!

#Matriz de Atraso de rede (em ms) entre o DC(i) e o PTT(j)
matrizAtraso = [[5,15,10],[20,8,10]] #Ex: 12 é o atraso (em ms) do DC_2 e PTT1
#Transforma a Matriz de Atraso em um dicionário de Atrasos!! (Facilita a definição do prob)
atrasos = makeDict([dcList,pttList],matrizAtraso,0)

#Orçamento total (em Reais) para o projeto
H = 50000

#Variáveis de Decisão
#Xij E {0,1} - Indica se DC(i) é atendido pelo PTT(j)
#Yj E {0,1} - Indica se PTT(j) vai ser "ativado"
#Função Objetivo : Minimizar o máximo atraso

#Definição do Problema
prob = LpProblem("Minimizar_Atraso_Max_DCs_PPTs",LpMinimize)
#Criação de Variável X a partir das Listas!! OBS: Xij E {0,1} - Indica se DC(i) é atendido pelo PTT(j)
variaveisX = LpVariable.dicts("X",(dcList,pttList),0,None,LpInteger)
#Exemplo de acesso ao dicionario das variaveis: print(variaveisX["DC_1"]["PTT_1"])

#Criação de Variável Y a partir das Listas!! Obs: Yi E {0,1} - Indica se PTT vai ser "ativado"
variaveisY = LpVariable.dicts("Y",pttList,0,None,LpInteger)

#Criação de tuplas para representar as variáveis (Utilizadas apenas p/ definição da função objetivo)
tuplasDCPTT = [(dc,ptt) for dc in dcList for ptt in pttList] #Ex: ("DC_1","PTT_1")

#Definição da Função Objetivo!
prob += lpSum([atrasos[dc][ptt]*variaveisX[dc][ptt] for (dc,ptt) in tuplasDCPTT]),"Custo"

#Restrições para cada elemento atrasos[dc][ptt]*variaveisX[dc][ptt]
for (dc,ptt) in tuplasDCPTT:
    prob += atrasos[dc][ptt]*variaveisX[dc][ptt] <= atrasos[dc][ptt],"restricoes_atrasos_%s_%s"%(dc,ptt)

#Restrição de cálculo de Yj (saber se o PTT(j) será ativado!!)
for ptt in pttList:
    prob += [variaveisX[dc][ptt] for dc in dcList] <= variaveisY[ptt],"Variavel_ativacao_PTT_%s"%ptt

#Restrição que um DC é suprido por apenas um PTT
for dc in dcList:
    prob += lpSum([variaveisX[dc][ptt] for ptt in pttList]) == 1,"Restricao_1PPTporDC_%s"%dc

#Restrições das capacidades dos PTTs
for ptt in pttList:
    prob += lpSum([variaveisX[dc][ptt]*trafegoDCs[dc] for dc in dcList]) <= capPtts[ptt],"Capacidade_%s"%ptt

#Restrição do custo total
var_aux = ""
for (dc,ptt) in tuplasDCPTT:
    var_aux += lpSum(custos[dc][ptt]*variaveisX[dc][ptt] + variaveisY[ptt]*custoAtivacaoPtts[ptt])
    # prob += lpSum(custos[dc][ptt]*variaveisX[dc][ptt] + variaveisY[ptt]*custoAtivacaoPtts[ptt]) <= H,"restricoes_valor_total_%s_%s"%(dc,ptt)
prob += var_aux <= H,"restricao_valor_total"
#Demais comandos!
prob.writeLP("Minimizar_Atraso_Max_DCs_PPTs.lp")
prob.solve()
print("Status:",LpStatus[prob.status])

for v in prob.variables():
    print(v.name,"=",v.varValue)

print("O menor somatório dos atrasos eh = ", value(prob.objective))





