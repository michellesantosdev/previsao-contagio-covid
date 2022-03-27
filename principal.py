from modelo.novos_casos_csv import NovosCasosCovidCsv


novos_casos_arquivo_csv = NovosCasosCovidCsv()
novos_casos_arquivo_csv.preencher_arquivo_csv('new_cases.csv')

print(novos_casos_arquivo_csv)
