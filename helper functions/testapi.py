import requests

# Make a GET request to the API endpoint
response = requests.get('http://127.0.0.1:8000/calendar/week-28-2023/')

# Check the response status code
print(response.status_code)

# Print the response content
print(response.json())

