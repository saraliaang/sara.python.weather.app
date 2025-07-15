import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string)
    formatted_date = dt.strftime("%A %d %B %Y")
    print(formatted_date)
    return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_f = float(temp_in_fahrenheit)
    temp_in_c = (temp_in_f-32)*5/9
    return round(temp_in_c, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total_value = 0
    for index, value in enumerate(weather_data):
        total_value+=float(value)
    return float(total_value/(index+1))


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    cell=[]
    list_return = []
    with open(csv_file,'r') as file:
        reader = file.read()
        lines = reader.splitlines()
        lines.pop(0)
        for i, row in enumerate(lines):
            if row != '':
                cell = row.split(',')
                cell[1] = int(cell[1])
                cell[2] = int(cell[2])
                list_return.append(cell)
        
    return list_return 
        


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data == []:
        return ()
    else:
        min = weather_data[0]
        min_place = 0
        for i, value in enumerate(weather_data):
            if value <= min:
                min = value
                min_place = i

        return float(min),min_place



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data == []:
        return ()
    else:
        max = weather_data[0]
        max_place = 0
        for i, value in enumerate(weather_data):
            if value >= max:
                max = value
                max_place = i
        
        return float(max),max_place


        


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


    low_list = []
    high_list = []
    day_count = 0
    for i in weather_data:
        low_list.append(i[1])
        high_list.append(i[2])
        day_count+=1

    low,low_index = find_min(low_list)
    high,high_index = find_max(high_list)
    average_low = calculate_mean(low_list)
    average_high = calculate_mean(high_list)
    date_low = convert_date(weather_data[low_index][0])
    date_high = convert_date(weather_data[high_index][0])
    
    low_in_celcius = convert_f_to_c(low)
    high_in_celcius = convert_f_to_c(high)
    average_high_in_celsius = convert_f_to_c(average_high)
    average_low_in_celsius = convert_f_to_c(average_low)
    
    formated_low = format_temperature(low_in_celcius)
    formated_high = format_temperature(high_in_celcius)
    formated_avg_high = format_temperature(average_high_in_celsius)
    formated_avg_low = format_temperature(average_low_in_celsius)


    summary = f'{day_count} Day Overview\n  The lowest temperature will be {formated_low}, and will occur on {date_low}.\n  The highest temperature will be {formated_high}, and will occur on {date_high}.\n  The average low this week is {formated_avg_low}.\n  The average high this week is {formated_avg_high}.\n'
    return summary
    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary=''
    for i in weather_data:
        low = format_temperature(convert_f_to_c(i[1]))
        high = format_temperature(convert_f_to_c(i[2]))
        date = convert_date(i[0])
        daily_summary += f'---- {date} ----\n  Minimum Temperature: {low}\n  Maximum Temperature: {high}\n\n'

    return daily_summary