import os 
from flask import Flask,  jsonify, render_template, request
import json 


app = Flask(__name__)


countryData = {}
alphaCode3 = {}
with open('./alphaCode3.json','r') as f:
    alphaCode3 = json.load(f)

with open('./countries.json','r') as f:
    countryData = json.load(f)
 
@app.route('/')
def homePage():
     return render_template('home.html')



@app.route('/<str>')
def hello_world(str):

    # try:
             
        userCountry = str.title()
        print(userCountry)
        alphaCodeValue = alphaCode3[userCountry]
        borders = countryData[alphaCodeValue]['countryBorders']
        bordersFlags = []
        for border in borders:
             bordersFlags.append([countryData[border]['Name'], countryData[border]['countryFlagImg']])
             
        country_Details_Dict = {
             'name' : countryData[alphaCodeValue]['Name'],
             'capital': countryData[alphaCodeValue]['capital'],
             'flag': countryData[alphaCodeValue]['countryFlagImg'],
             'population': countryData[alphaCodeValue]['population'],
             'area': countryData[alphaCodeValue]['Area'],
             'latitude': countryData[alphaCodeValue]['latitude'],
             'longitude': countryData[alphaCodeValue]['longitude'],
             'borderFlags': bordersFlags 
        }
        print(countryData[alphaCodeValue]['Name'])
        print(countryData[alphaCodeValue]['capital'])
        print(countryData[alphaCodeValue]['countryFlagImg'])
        # print(countryData[alphaCodeValue]['countryBorders'])
        print(country_Details_Dict['borderFlags'])
        return render_template('circle.html',params=country_Details_Dict)
    # except Exception as e:
    #      print("The exception is ",e)

 

#  Pavan Code
@app.route("/countrycca3/<str>")
def countrycca3(str):
    return jsonify(countryData[str.upper()])

@app.route("/country/")
def AllCountryDetails():  
    return jsonify(countryData)


@app.route("/country/<str>")
def countryDetails(str):
        UserCountry = str.title()
        alphaCodeValue = alphaCode3[UserCountry]
        return jsonify(countryData[alphaCodeValue])


if __name__ == '__main__':
    app.run(debug=True,port=5003) 


