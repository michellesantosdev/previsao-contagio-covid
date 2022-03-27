class NovosCasosCovidCsv:

    def __init__(self):
        self.data = []
        self.quantidade_casos = []

    @staticmethod
    def ler_arquivo_csv(nome_arquivo):
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            return linhas

    def preencher_arquivo_csv(self, nome_arquivo):
        linhas = self.ler_arquivo_csv(nome_arquivo)

        for linha in linhas[1:]:
            campos_separados = linha.split(',')

            self.data.append(campos_separados[0])
            self.quantidade_casos.append(campos_separados[1])
