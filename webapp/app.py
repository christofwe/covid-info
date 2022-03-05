import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/covid')
def covid():

    my_state = 'BY' # Bayern
    my_district = '09375' # LK Regensburg

    district = requests.get(f"https://api.corona-zahlen.org/districts/{my_district}").json()
    state = requests.get(f"https://api.corona-zahlen.org/states/{my_state}").json()

    templateData = {
        'd_county' : district['data'][my_district]['county'],
        'd_population' : district['data'][my_district]['population'],
        'd_lastUpdate' : district['meta']['lastUpdate'],
        'd_cases' : district['data'][my_district]['cases'],
        'd_casesPerWeek' : district['data'][my_district]['casesPerWeek'],
        'd_delta_cases' : district['data'][my_district]['delta']['cases'],
        'd_deaths' : district['data'][my_district]['deaths'],
        'd_weekIncidence' : format(district['data'][my_district]['weekIncidence'], '.1f'),
        's_state' : state['data'][my_state]['name'],
        's_population' : state['data'][my_state]['population'],
        's_cases' : state['data'][my_state]['cases'],
        's_casesPerWeek' : state['data'][my_state]['casesPerWeek'],
        's_delta_cases' : state['data'][my_state]['delta']['cases'],
        's_weekIncidence' : format(state['data'][my_state]['weekIncidence'], '.1f'),
        's_hospitalization_incidence7Days' : format(state['data'][my_state]['hospitalization']['incidence7Days'], '.1f')
    }

    return render_template('covid.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
