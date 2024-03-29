import pandas
from fbprophet import Prophet


def prever_casos_futuros(novos_casos_covid_csv, dias):
    quadro_de_dados = pandas.DataFrame(novos_casos_covid_csv.data, novos_casos_covid_csv.quantidade_casos)
    quadro_de_dados = quadro_de_dados.reset_index(0)
    quadro_de_dados.columns = ['y', 'ds']

    modelo = Prophet()
    modelo.fit(quadro_de_dados)

    quadro_de_dados_futuro = modelo.make_future_dataframe(periods=dias)
    previsao = modelo.predict(quadro_de_dados_futuro)
    return previsao


def mostrar_previsao(previsao, dias):
    previsao_dias = ''
    for index, yhat in enumerate(previsao.yhat[-dias:]):
        previsao_dias += f'{index+1} -> {round(yhat)}\n'

    return previsao_dias
