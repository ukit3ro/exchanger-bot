import requests
data = requests.get('https://openexchangerates.org/api/latest.json?app_id=83cb1073284143dc8d1ff26e9e13a6c3&base=USD&symbols=RUB').json()
print (data['rates']['RUB'])
this_token = '5729607125:AAGL9Dw7czWp7X7SDDbHk1Nyn-StfhslMfI'