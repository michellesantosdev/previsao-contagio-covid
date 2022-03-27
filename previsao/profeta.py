import pandas
from fbprophet import Prophet


def prever_casos_futuros(novos_casos_covid_csv):
    quadro_de_dados = pandas.DataFrame(novos_casos_covid_csv.data, novos_casos_covid_csv.quantidade_casos)
    quadro_de_dados = quadro_de_dados.reset_index(0)
    quadro_de_dados.columns = ['y', 'ds']

    modelo = Prophet()
    modelo.fit(quadro_de_dados)

    quadro_de_dados_futuro = modelo.make_future_dataframe(periods=4)
    previsao = modelo.predict(quadro_de_dados_futuro)
    mostrar_previsao(previsao)


def mostrar_previsao(previsao):
    for index, yhat in enumerate(previsao.yhat[-4:]):
        print(f'{index+1} -> {round(yhat)}')
