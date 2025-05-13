import requests
import pandas as pd
import plotly.express as px

# 1. Fetch data from public API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

# 2. Create a DataFrame
df = pd.json_normalize(data)

# 3. Select relevant columns
df = df[[
    'country', 
    'cases', 
    'todayCases', 
    'deaths', 
    'todayDeaths', 
    'recovered', 
    'active', 
    'critical', 
    'countryInfo.lat', 
    'countryInfo.long'
]]

df.rename(columns={
    'country': 'Country',
    'cases': 'Total Cases',
    'todayCases': 'Today Cases',
    'deaths': 'Total Deaths',
    'todayDeaths': 'Today Deaths',
    'recovered': 'Recovered',
    'active': 'Active Cases',
    'critical': 'Critical Cases',
    'countryInfo.lat': 'Latitude',
    'countryInfo.long': 'Longitude'
}, inplace=True)

# 4. Show data preview
print(df.head())

# 5. Plot total cases using Plotly (interactive world map)
fig = px.scatter_geo(
    df,
    lat='Latitude',
    lon='Longitude',
    hover_name='Country',
    size='Total Cases',
    color='Total Cases',
    projection='natural earth',
    title='🌍 COVID-19 Global Total Cases (Live)',
    template='plotly_dark',
    color_continuous_scale='Reds'
)

fig.show()
