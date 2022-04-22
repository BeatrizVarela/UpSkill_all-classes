"""
Escreva em linguagem Python um programa que leia uma data (ano, mês e dia
em separado) e um número inteiro x, e devolva uma nova data x dias mais à
frente.
"""

ano = int(input("ano: "))
mes = int(input("mês: "))
dia = int(input("dia: "))
dias_add = int(input("que dia será daqui a este número de dias? "))

meses_dias = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}

e_ano_bisexto = (mes == 2 and ano % 4 == 0 and not (ano % 400 == 0 and ano % 100 == 0))
dias_do_mes = meses_dias[mes] + e_ano_bisexto # you can add boolean expressions to numbers, as if True it will be interpreted as one and if False it will be interpreted as 0

while dia + dias_add > dias_do_mes:
    ano += (mes + 1) > 12 # é adicionado um se o proximo mês for menor que 12 (Dezembro)
    mes = (mes + 1) % 12 if mes + 1 > 12 else mes + 1 # se o mês for maior que doze incrementamos o mês o obtemos o resto da divisão (ex: mês = 13 então mês % 12 = 1)
    dias_add -= dias_do_mes - dia # removemos os restantes dias que faltam no mês dos dias adicionados
    dia = 0 # pomos o dia como 0 para adicionar-mos os restantes dias adicionais caso saia do loop ou no próximo loop sem ter um dia a mais
    dias_do_mes = meses_dias[mes] + e_ano_bisexto # atualizamos os dias do mês

dia += dias_add # adicionamos os restantes dias do mês

print(f"{ano}-{mes}-{dia}")