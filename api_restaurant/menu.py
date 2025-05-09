import requests

url_top_10 = r'http://127.0.0.1:8000/api/top_10_by_price/'
url_menu = r'http://127.0.0.1:8000/api/menu/'
url_breakfasts = r'http://127.0.0.1:8000/api/breakfasts/'
url_soups = r'http://127.0.0.1:8000/api/soups/'
url_beverages = r'http://127.0.0.1:8000/api/beverages/'
url_desserts = r'http://127.0.0.1:8000/api/desserts/'
url_starters = r'http://127.0.0.1:8000/api/starters/'
url_main_courses = r'http://127.0.0.1:8000/api/main_courses/'

def get_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data