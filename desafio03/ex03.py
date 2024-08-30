import json

#carregamento de dados
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

#extraindo valores e filtrando dias acima de 0 reais de faturamento
faturamentoDiario = [dia["valor"] for dia in dados["faturamento diario"] if dia["valor"] > 0]


menorFaturamento = min(faturamentoDiario)

maiorFaturamento = max(faturamentoDiario)

mediaMensal = sum(faturamentoDiario) / len(faturamentoDiario)

diasAcimaDaMedia = sum(1 for valor in faturamentoDiario if valor > mediaMensal)

print("Menor valor de faturamento ocorrido em um dia do mês: R${:.2f}".format(menorFaturamento))
print("Maior valor de faturamento ocorrido em um dia do mês: R${:.2f}".format(maiorFaturamento))
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {}".format(diasAcimaDaMedia))
