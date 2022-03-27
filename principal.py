from modelo.novos_casos_csv import NovosCasosCovidCsv
from previsao.profeta import prever_casos_futuros


novos_casos_arquivo_csv = NovosCasosCovidCsv()
novos_casos_arquivo_csv.preencher_arquivo_csv('new_cases.csv')

prever_casos_futuros(novos_casos_arquivo_csv)
