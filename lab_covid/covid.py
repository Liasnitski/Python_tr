import pandas as pd
import plotly.express as px

data = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv',
                 parse_dates=['Date'])


data = data[data['Country'].isin(['Belarus'])]

data['Cases'] = data[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)
data['New_cases'] = data["Cases"].diff()

cases = px.area(data, x='Date', y='Cases', title='Belarus')
cases.show()
cases1= px.area(data, x='Date', y='New_cases', title='NewBelarus')
cases1.show()
