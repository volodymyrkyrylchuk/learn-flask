from flask import Flask
from flask import request

app = Flask(__name__)

# use Python Dict as DB
storage = dict()
# structure of storage: key - username, value - dict(default empty) in future will contain info about current user


# put some default users into db
storage.update(
    {
        "Kelly": {},
        "Nelly": {},
        "Shelly": {},
        "Belly": {}
    }
)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users/list/')
def user_list():
    username_list = storage.keys()
    return '<br>'.join(username_list)


@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return f'User {username} was deleted'
    else:
        return 'User doesn`t exist or already deleted'


# # add user with GET method
# @app.route('/users/add/<username>')
# def add_user_get(username):
#     return_string = f'User {username} was added'
#     if username in storage:
#         return_string = f'User {username} was rewritten'
#     storage[username] = {}
#     return return_string


# add user with POST method
@app.route('/users/add/', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        return_string = f'User {username} was added'

        if username in storage:
            return_string = f'User {username} was rewritten'

        if username:
            storage[username] = {}
        else:
            return_string = 'Put user name!'

        return return_string

    return '''<form method="POST">
                  User name: <input type="text" name="username"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''