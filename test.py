import requests
import json

url = "https://api.contactout.com/v1/company/search"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'basic',
    'token': 'lC3hMrT7kKHZGrND76nwF8zI'
}
data = {
    "page": 1,
    "name": ["google"],
    # "domain": ["google.com"],
    # "size": ["1_10"],
    # "hq_only": False,
    # "location": ["United States"],
    # "industry": ["Software"],
    # "min_revenue": 1000000,
    # "max_revenue": 50000000,
    # "year_founded_from": 2000,
    # "year_founded_to": 2024
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
