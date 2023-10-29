import json
import os

os.chdir('./KnowTheNation/others/')

alphaCode3 = {}

with open('./countries.json','r',errors='ignore',encoding='utf-8') as f:
    countriesData = json.load(f)


for country in countriesData:
    try:
        
        alphaCode = country
        countryName = countriesData[country]['Name']
        alphaCode3[countryName] = alphaCode

    except Exception as e:
        print(country['Name'],e)

with open('alphaCode3.json','w',encoding='utf-8') as f:
    json.dump(alphaCode3,f)

