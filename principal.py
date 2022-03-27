from modelo.novos_casos_csv import NovosCasosCovidCsv
from previsao.profeta import prever_casos_futuros, mostrar_previsao


def input_dias():
    dias = input('Digite um número inteiro de dias para prever : ')
    while not dias.isnumeric():
        dias = input('Valor inválido! Digite um número inteiro de dias para prever : ')
    return int(dias)


novos_casos_arquivo_csv = NovosCasosCovidCsv()
novos_casos_arquivo_csv.preencher_arquivo_csv('new_cases.csv')
dias = input_dias()
previsao = prever_casos_futuros(novos_casos_arquivo_csv, dias)
print(mostrar_previsao(previsao, dias))
