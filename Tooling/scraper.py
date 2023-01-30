import requests
r = requests.get('https://api.github.com/user', auth=('<email@email.comm>', '<password>'))
print(r.text)
print(r.status_code)

