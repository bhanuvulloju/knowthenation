import requests
import json

countriesDict = {}

with open('./APIcountriesRaw.json','r',errors='ignore',encoding='utf-8') as f:
    countriesData = json.load(f)

count = 0
for country in countriesData:
    try:
        countryName = country['name']['common']
        countryCurrency = country['currencies']
        countryCapital = country['capital'][0]
        countryLanguages = country['languages']
        countryLatitudeLongitude = country['latlng']
        countryBorders = country.get('borders') if country.get('borders') else []
        
        # print(f"{countryName}-{countryCapital}-{countryCurrency}-{countryArea}-{countryBorders}")
        countriesDict[country['cca3']] ={
            'Name' : countryName,
            'capital' : countryCapital,
            'currency' : countryCurrency,
            'languages': countryLanguages,
            'latitude': country['latlng'][0],
            'longitude': country['latlng'][1],
            'Area' : country['area'],
            'population' : country['population'],
             'countryFlagImg' : country['flags']['png'],
            'countryBorders': countryBorders
        }
        count += 1
        # if count == 5:
        #     break
    except Exception as e:
        print(country['name']['common'],e)

with open('temp.json','w',encoding='utf-8') as f:
    json.dump(countriesDict,f)



