"""
Bot Module for API
"""
from os.path import join, dirname
import os
import requests
from dotenv import load_dotenv

def get_result_from_api(text):
    """Main Method"""
    if text == "!!covid":
        dotenv_path = join(dirname(__file__), 'sql.env')
        load_dotenv(dotenv_path)
        url = "https://rapidapi.p.rapidapi.com/v1/total"
        covid_api_key = os.environ['covidapikey']

        querystring = {"country":"USA"}

        headers = {
            'Content-Type': 'application/json',
            'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
            'x-rapidapi-key': covid_api_key
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            return "Recovered in USA: " + str(response.json()['data']['recovered'])
        return None

    headers = {'Content-Type': 'application/json'}
    api_url = 'https://api.funtranslations.com/translate/valspeak.json?text=' + text[14:]

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()['contents']['translated']
    return None
