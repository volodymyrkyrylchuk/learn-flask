from flask import Flask, request

app = Flask(__name__)

# use Python Dict as DB
storage = dict()
# structure of storage: key - username, value - dict(default empty) in future will contain info about current user


# put some default users into db
storage.update(
    {
        "username1": {},
        "username2": {},
        "username3": {},
        "username4": {}
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


@app.route('/users/add/', methods=['GET', 'POST'])
def add_new_user():
    if request.method == 'POST':
        username = request.form.get('username')
        new_user = f'User {username} was added'
        if username in storage:
            new_user = f'User {username} was re-added'
        storage[username] = {}
        return new_user

    return '''<form method="POST">
                  User name: <input type="text" name="username"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''
app.run()
