import requests
response= requests.get("https://api.github.com/users/jetcanine/repos")
# print(response.json())
projects= response.json()

for content in projects:
    print(f"Project Name : {content['name']} Project URL: {content['html_url']}")