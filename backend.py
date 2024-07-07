import requests
API_KEY = "db36ab3300a242ee5de21b96ff20b055"
def get_data(place, forecast_days=None,):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 *forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place= "Tokyo", forecast_days=3))