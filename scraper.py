# Initally started with help from ChatGPT
import requests
token = ""
with open('api-token.txt', 'r') as file:
    token = file.readline()

url = "https://www.robotevents.test/api/v2/programs?id%5B%5D=185"
headers = {"Content-Type":"application/json","Authorization": f"Bearer {token}"}
response = requests.get(url, data={}, headers=headers)


if response.status_code == 200:
    # API call was successful
    data = response.json()  # Convert the response to a Python object
    print(data)
    # Process the data as needed
else:
    # API call failed
    print(f"Error {response.status_code}: {response.text}")