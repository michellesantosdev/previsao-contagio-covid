from modelo.novos_casos_csv import NovosCasosCovidCsv
from previsao.profeta import prever_casos_futuros, mostrar_previsao


def test_deve_gerar_previsao():
    novos_casos_covid_csv = NovosCasosCovidCsv()
    novos_casos_covid_csv.preencher_arquivo_csv('tests/new_cases_test.csv')

    dias = 4
    previsao = prever_casos_futuros(novos_casos_covid_csv, dias)
    previsao_dias = mostrar_previsao(previsao, dias)

    assert previsao_dias == '1 -> 7\n2 -> 8\n3 -> 9\n4 -> 10\n'
