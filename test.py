import requests
url='https://v6.exchangerate-api.com/v6/6c4dc57c77cb4108b4df8583/latest/USD'
response=requests.get(url)
result=response.json()
print(result['conversion_rates'])
x=result['conversion_rates']['USD']
y=result['conversion_rates']['BGN']
print(x,y)
