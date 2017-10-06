import requests

class Average():

    def get_avg_temperature(filters=None):
        # define standard valid services that are used for caculate average temperature
	    standard_service_list = ['noaa', 'weatherdotcom', 'accuweather']

	    # get the user-input service list from filters
	    filter_list = filters.split(',')

	    # define a list to hold the valid services
	    service_list = []
	    for s in filter_list:
		    if s in standard_service_list:
			    service_list.append(s)

	    # get temperature list from valid service list
	    temperature_dict = {}
	    for service in service_list:
		    temp = get_temperature(service)
		    temperature_dict[service] = temp

	    # calculate average temprature dict
	    average = get_average(temperature_dict)

	    return average


    # get temperature dic from a service
    def get_temperature(service=None):
	    url = ''
	    if (service == 'noaa'):
		    url = 'http://127.0.0.1:5000/noaa?latlon=44,33'
		    #response = requests.get(url)
	    elif (service == 'accuweather'):
		    url = 'http://127.0.0.1:5000/accuweather?latitude=44&longitude=33'
		    #response = requests.get(url)
	    elif (service == 'weatherdotcom'):
		    url = 'http://127.0.0.1:5000/weatherdotcom {"lat":33.3,"lon":44.4}'
		    #response = requests.post(url)

	    response = requests.get(url)
	    if (response.status_code == 200):
		    data = response.json()
	    else:
		    data = {}

	    return data


    # calculate average temperature from a dictionary of temperatures
    def get_average(dict=None):

        average = {}
        current = {}
        high = {}
        low = {}
        current_f = []
        current_c = []
        high_f = []
        high_c = []
        low_f = []
        low_c = []

        if (dict.has_key("noaa")):
            if (len(dict["noaa"]) != 0):
                current_f.append(dict["noaa"]["today"]["current"]["fahrenheit"])
                current_c.append(dict["noaa"]["today"]["current"]["celsius"])
                high_f.append(dict["noaa"]["today"]["high"]["fahrenheit"])
                high_c.append(dict["noaa"]["today"]["high"]["celsius"])
                low_f.append(dict["noaa"]["today"]["low"]["fahrenheit"])
                low_c.append(dict["noaa"]["today"]["low"]["celsius"])

        if (dict.has_key("accuweather")):
            if (len(dict['accuweather']) != 0):
                current_f.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["current"]["fahrenheit"])
                current_c.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["current"]["celsius"])
                high_f.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["high"]["fahrenheit"])
                high_c.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["high"]["celsius"])
                low_f.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["low"]["fahrenheit"])
                low_c.append(dict["accuweather"]["simpleforecast"]["forecastday"][0]["low"]["celsius"])

        average_current_f = calculate_average(current_f)
        average_current_c = calculate_average(current_c)
        average_high_f = calculate_average(high_f)
        average_high_c = calculate_average(high_c)
        average_low_f = calculate_average(low_f)
        average_low_c = calculate_average(low_c)

        current["fahrenheit"] = average_current_f
        current["celsius"] = average_current_c
        high["fahrenheit"] = average_high_f
        high["celsius"] = average_high_c
        low["fahrenheit"] = average_low_f
        low["celsius"] = average_low_c

        average["current"] = current
        average["high"] = high
        average["low"] = low

        return average

    # calculate the average value with a list of values
    def calculate_average(list=None):
        sum = 0
        for e in list:
            sum += int(e)

        avg = sum / len(list)

        return avg

