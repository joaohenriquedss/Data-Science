# pip install pandas e fbprophet 
import pandas as pd
from fbprophet import Prophet

covid_data = pd.read_csv('brazil2.csv') # dataset

def normalizer_date(date):
    result = ''
    for i in range(10):
        result += date[i]
    return result

def normalizer_results(num):
    result = int(num)
    return result

def predicao(covid_data):
  covid_data['date'] = covid_data.date.apply(normalizer_date)
  covid_data['date'] = pd.to_datetime(covid_data['date'])
  covid_newDeaths = covid_data[['date','newDeaths']]
  covid_newDeaths.columns = ['ds','y']

  m = Prophet(interval_width= 0.90)
  m.fit(covid_newDeaths)
  predicao = m.make_future_dataframe(periods=7)

  previsao = m.predict(predicao)

  data = previsao[['ds','yhat_lower','yhat','yhat_upper']].tail(7)

  data.columns = ['data','previsao_baixa','previsao_media','previsao_alta']



  data['previsao_baixa'] = data.previsao_baixa.apply(normalizer_results)
  data['previsao_media'] = data.previsao_media.apply(normalizer_results)
  data['previsao_alta'] = data.previsao_alta.apply(normalizer_results)
  return data

pred = predicao(covid_data)
print(pred)
print()
print(pred['previsao_media'])
