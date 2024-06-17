import requests
from bs4 import BeautifulSoup


#https://www.metoffice.gov.uk/weather/maps-and-charts/temperature-map#?bbox=[[50.37699944702328,-2.8372192382812504],[52.29000260620264,2.4362182617187504]]&model=ukmo-ukv&layer=temperature&timestep=1707303600000&search=SE1&slatlong=51.49817705154419%2C-0.09113073348999023

def scrape_met_office_weather(latitude, longitude, date):
    # URL format for historical weather data
    url = f"https://www.metoffice.gov.uk/weather/archive/{latitude},{longitude}/{date}/Daily"
    
    # Sending a GET request to the website
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting specific information, you may need to inspect the HTML structure of the website
        # and adjust this code accordingly to extract the data you need
        # For example, let's say we want to extract the maximum temperature
        max_temp = soup.find('span', class_='temperature high').text
        
        return max_temp
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None
    

def get_historical_weather(api_key, latitude, longitude, date):
    """
    Example usage: 
    
    api_key = "your_api_key"
    latitude = 51.5074  # London's latitude
    longitude = 0.1278  # London's longitude
    date = '2024-01-01'  # Example date

    weather_data = get_historical_weather(api_key, latitude, longitude, date)
    if weather_data:
        for hour in weather_data['forecast']['forecastday'][0]['hour']:
            print(hour['time'], hour['temp_c'])
    """
    url = f"http://api.weatherapi.com/v1/history.json?key={api_key}&q={latitude},{longitude}&dt={date}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

