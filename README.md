# previsao-contagio-covid

D3 Challenge 

Sua missão é prever, dado um número de dias, a evolução do contágio por COVID-19 🦠 no mundo. 

Seu método deve receber um número inteiro (N) que representa a quantidade de dias, e rejeitar qualquer outro tipo de input, sendo: 

0 &lt; N
```
def predict(days=1):
    print("do stuff here")
```

 O output da sua função precisa dizer o número de dias à frente (calculado por D) e seu respectivo valor de casos.  
 Dado D=4, teremos:  
```
1 -> 456
2 -> 765
3 -> 40
4 -> 964
```


# Passo a passo para rodar a aplicação

Foi utilizado o Python 3.9 e o conda como gerenciamento de pacotes

## Instalar dependências
```
conda env update --file environment.yml --name base
```

## Executar aplicação
```
python principal.py
```

# Convenções de código e testes
## Rodar convenção de código
```
flake8
```

## Rodar testes
```
pytest
```

Obs: Ambos foram implementados no CI (Github Actions)

## Arquivo Entrada .csv
Foi utilizado o https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv como arquivo de entrada para apartir dele realizar as previsões

## Links que auxiliaram o desenvolvimento
- https://www.youtube.com/watch?v=qE4WJqTmwQ0&ab_channel=AnalistasQuant
- https://www.youtube.com/watch?v=7f4RJrPoJp8&ab_channel=TudoMaisConstante
- https://docs.conda.io/projects/conda/en/latest/index.html
- https://pypi.org/project/fbprophet/
- https://facebook.github.io/prophet/docs/quick_start.html
- https://pystan2.readthedocs.io/en/latest/windows.html
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually
