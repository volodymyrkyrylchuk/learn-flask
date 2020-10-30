from flask import Flask  # импортируем из библиотеки flask класс Flask
from flask import jsonify, request

app = Flask(__name__)  # создаем объект app на основе класса Flask, (__name__) - имя нашего файла

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
    return jsonify({'msg': 'Hello, World!'})


@app.route('/users/list/')
def user_list():
    return jsonify(storage)


@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return jsonify(message='User  was deleted')
    else:
        return jsonify (message='User doesnt exist or already deleted')


@app.route('/users/add/', methods=["POST"])
def add_user_list():
    data = request.get_json()  # get json return dict loaded from json body
    try:
        username = data['username']
    except Exception as e:
        response = {'msg': f'The field {e} is required'}
        username = False

    if username:
        storage[username] = dict()
        response = {'msg': 'user was added'}
    return jsonify(response)


if __name__ == '__main__':  # если запускается через файл app.py, то проект должен запуститься как flask приложение
    app.run(debug=True)  # запускается локальный сервер