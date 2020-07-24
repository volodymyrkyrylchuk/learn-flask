import requests


new_user = {
    'username': 'Bruce',
}

# response = requests.post('http://localhost:5000/users/add/', json=new_user)
#
# print(response.json())
response2 = requests.get('http://localhost:5000/users/delete/username2')
#print(response2.json())